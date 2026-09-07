#!/usr/bin/env bash
# Resize/convert all png|PNG|jpeg|jpg|JPG images under content/ to .jpg,
# long edge <= MAX_DIM px, file size <= MAX_BYTES, in place.
# Exception: PNGs already under PNG_KEEP_MAX_DIM px and PNG_KEEP_MAX_BYTES
# bytes are left as PNG, untouched.
# Exception: paths listed in EXCLUDE_RELATIVE (relative to content-dir) are
# always left untouched, regardless of size/dimensions.
# Non-image documents (.docx, .odp, etc.) are never in scope: the file
# search below only ever matches png/PNG/jpeg/jpg/JPG, so such files are
# never read or written by this script.
# Updates filename references in content/**/*.md when a file gets renamed.
#
# Usage: scripts/resize-and-convert-images.sh [content-dir] --apply
#        scripts/resize-and-convert-images.sh [content-dir]          (dry run, default)
#
# SAFETY: this script defaults to a dry run and changes NOTHING unless you
# pass --apply explicitly. Unknown arguments are a hard error, not silently
# ignored, so a typo can never turn a dry run into a real run.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTENT_DIR="$SCRIPT_DIR/../content"
MAX_DIM=1600
MAX_BYTES=307200   # 300 KiB
PNG_KEEP_MAX_DIM=1600
PNG_KEEP_MAX_BYTES=204800   # 200 KiB
DRY_RUN=1
CONTENT_DIR_SET=0

# Paths relative to content-dir that must never be converted or renamed,
# no matter their size or dimensions.
EXCLUDE_RELATIVE=(
  "de/posts/2024-08-05-hello-world/comenius-institut-logo.png"
)

usage() {
  echo "Usage: $0 [content-dir] --apply" >&2
  echo "       $0 [content-dir]           # dry run (default, no changes written)" >&2
}

for arg in "$@"; do
  case "$arg" in
    --apply) DRY_RUN=0 ;;
    --dry-run) DRY_RUN=1 ;;
    --help|-h) usage; exit 0 ;;
    -*)
      echo "Error: unknown option '$arg'" >&2
      usage
      exit 1
      ;;
    *)
      if [ "$CONTENT_DIR_SET" -eq 1 ]; then
        echo "Error: unexpected extra argument '$arg'" >&2
        usage
        exit 1
      fi
      CONTENT_DIR="$arg"
      CONTENT_DIR_SET=1
      ;;
  esac
done

if ! command -v convert >/dev/null 2>&1; then
  echo "Error: ImageMagick 'convert' not found." >&2
  exit 1
fi
if ! command -v identify >/dev/null 2>&1; then
  echo "Error: ImageMagick 'identify' not found." >&2
  exit 1
fi
if [ ! -d "$CONTENT_DIR" ]; then
  echo "Error: content dir '$CONTENT_DIR' not found." >&2
  exit 1
fi
CONTENT_DIR="${CONTENT_DIR%/}"

is_excluded() {
  local rel="$1" ex
  for ex in "${EXCLUDE_RELATIVE[@]}"; do
    [ "$rel" = "$ex" ] && return 0
  done
  return 1
}

converted=0
renamed_only=0
skipped_ok=0
skipped_png_small=0
skipped_excluded=0
skipped_collision=0
still_too_big=0
errors=0
collision_files=()

mapfile -d '' files < <(find "$CONTENT_DIR" -type f \
  \( -name '*.png' -o -name '*.PNG' -o -name '*.jpeg' -o -name '*.jpg' -o -name '*.JPG' \) -print0 | sort -z)

total=${#files[@]}
echo "Found $total image(s) under $CONTENT_DIR"
[ "$DRY_RUN" -eq 1 ] && echo "(dry run — no files will be changed)"
echo

update_refs() {
  # $1 old basename, $2 new basename, $3 directory to search (content root)
  # Only rewrites the filename when it is a bare local reference or part of
  # an oer.community URL. Any occurrence inside a URL to a DIFFERENT domain
  # (e.g. a coincidentally identical WordPress upload filename mirrored on
  # some unrelated site) is left untouched. Also only matches the filename
  # as a whole token, so a short name like "2.jpg" can't match inside an
  # unrelated "22.jpg".
  local old="$1" new="$2" root="$3"
  local mdfile before after
  grep -rlF -- "$old" "$root" --include='*.md' 2>/dev/null | while IFS= read -r mdfile; do
    before=$(md5sum "$mdfile")
    OLD="$old" NEW="$new" perl -i -pe '
      # 1) stash every non-oer.community URL, replacing it with a NUL
      #    placeholder (\x00 = NUL byte, never occurs in real text).
      #    \x27 = escaped single quote, needed since this whole script
      #    is itself inside single quotes on the bash side.
      my @foreign_urls;
      s{(https?://[^\s()<>"\x27]*)}{
        my $url = $1;
        $url =~ /oer\.community/ ? $url
          : (push(@foreign_urls, $url), "\x00" . $#foreign_urls . "\x00");
      }ge;

      # 2) rename the old filename as a whole word only (foreign URLs
      #    are gone now, so this cannot touch them).
      s/(?<![\w-])\Q$ENV{OLD}\E(?![\w-])/$ENV{NEW}/g;

      # 3) restore the stashed URLs.
      s{\x00(\d+)\x00}{ $foreign_urls[$1] }ge;
    ' "$mdfile"
    after=$(md5sum "$mdfile")
    if [ "$before" != "$after" ]; then
      echo "    updated reference in $mdfile"
    else
      echo "    left untouched (only non-oer.community reference found) in $mdfile"
    fi
  done
}

i=0
for src in "${files[@]}"; do
  i=$((i+1))
  dir=$(dirname "$src")
  base=$(basename "$src")
  stem="${base%.*}"
  ext="${base##*.}"
  target="$dir/$stem.jpg"

  printf '[%d/%d] %s\n' "$i" "$total" "$src"

  rel="${src#$CONTENT_DIR/}"
  if is_excluded "$rel"; then
    echo "  excluded by config, leaving untouched"
    skipped_excluded=$((skipped_excluded+1))
    continue
  fi

  fmt=""
  if [ "$ext" = "png" ] || [ "$ext" = "PNG" ]; then
    w=$(identify -format '%w' "$src" 2>/dev/null)
    h=$(identify -format '%h' "$src" 2>/dev/null)
    size=$(stat -c%s "$src")
    longedge=$(( w > h ? w : h ))
    if [ "$longedge" -lt "$PNG_KEEP_MAX_DIM" ] && [ "$size" -lt "$PNG_KEEP_MAX_BYTES" ]; then
      echo "  small PNG (${w}x${h}, ${size} bytes) below keep-as-is threshold, leaving untouched"
      skipped_png_small=$((skipped_png_small+1))
      continue
    fi
  else
    fmt=$(identify -format '%m' "$src" 2>/dev/null | head -c4)
  fi

  if [ "$fmt" = "JPEG" ]; then
    w=$(identify -format '%w' "$src" 2>/dev/null)
    h=$(identify -format '%h' "$src" 2>/dev/null)
    size=$(stat -c%s "$src")
    longedge=$(( w > h ? w : h ))
    if [ "$longedge" -le "$MAX_DIM" ] && [ "$size" -le "$MAX_BYTES" ]; then
      if [ "$target" = "$src" ]; then
        echo "  already compliant, skipping"
        skipped_ok=$((skipped_ok+1))
      else
        if [ -e "$target" ]; then
          echo "  COLLISION: '$src' -> target '$target' already exists — skipping, needs manual review"
          skipped_collision=$((skipped_collision+1))
          collision_files+=("$src -> $target (target already exists)")
        elif [ "$DRY_RUN" -eq 1 ]; then
          echo "  would rename (no re-encode needed) -> $target"
        else
          mv -f "$src" "$target"
          update_refs "$base" "$stem.jpg" "$CONTENT_DIR"
          renamed_only=$((renamed_only+1))
          echo "  renamed (already compliant) -> $target"
        fi
      fi
      continue
    fi
  fi

  if [ "$target" != "$src" ] && [ -e "$target" ]; then
    echo "  COLLISION: '$src' -> target '$target' already exists — skipping, needs manual review"
    skipped_collision=$((skipped_collision+1))
    collision_files+=("$src -> $target (target already exists)")
    continue
  fi

  if [ "$DRY_RUN" -eq 1 ]; then
    echo "  would convert -> $target"
    continue
  fi

  tmp=$(mktemp --suffix=.jpg "${dir}/.rsz-XXXXXX")

  quality=85
  dim=$MAX_DIM
  status=0
  while :; do
    if ! err=$(convert "$src" -auto-orient -background white -alpha remove -alpha off \
        -resize "${dim}x${dim}>" -strip -sampling-factor 4:2:0 -quality "$quality" "$tmp" 2>&1); then
      echo "  ERROR converting $src: $err" >&2
      rm -f "$tmp"
      status=-1
      break
    fi
    size=$(stat -c%s "$tmp")
    if [ "$size" -le "$MAX_BYTES" ]; then
      status=1
      break
    fi
    if [ "$quality" -gt 40 ]; then
      quality=$((quality-5))
      continue
    fi
    if [ "$dim" -gt 800 ]; then
      dim=$((dim-160))
      quality=70
      continue
    fi
    status=2
    break
  done

  if [ "$status" -eq -1 ]; then
    errors=$((errors+1))
    continue
  fi

  if [ "$status" -eq 2 ]; then
    finalsize=$(stat -c%s "$tmp")
    echo "  WARNING: could not get under $MAX_BYTES bytes (final ${finalsize} bytes, quality=$quality, dim=$dim)" >&2
    still_too_big=$((still_too_big+1))
  fi

  mv -f "$tmp" "$target"
  converted=$((converted+1))
  echo "  converted -> $target ($(stat -c%s "$target") bytes)"

  if [ "$target" != "$src" ]; then
    rm -f "$src"
    update_refs "$base" "$stem.jpg" "$CONTENT_DIR"
  fi
done

echo
echo "Done."
echo "  converted (re-encoded): $converted"
echo "  renamed only (already compliant): $renamed_only"
echo "  already compliant, untouched: $skipped_ok"
echo "  small PNGs kept as-is: $skipped_png_small"
echo "  excluded by config: $skipped_excluded"
echo "  skipped due to name collision: $skipped_collision"
if [ "${#collision_files[@]}" -gt 0 ]; then
  for f in "${collision_files[@]}"; do
    echo "    - $f"
  done
fi
echo "  still over size limit after max compression: $still_too_big"
echo "  errors: $errors"
