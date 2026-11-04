import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check  # noqa: E402


class Namen(unittest.TestCase):
    def test_namen_gebeugt(self):
        self.assertEqual(check.find_namen("Erikas Branch und Maxens Text", ("Erika", "Max")), ["Erikas", "Maxens"])

    def test_erlaubte_namen(self):
        self.assertEqual(check.find_namen("Max Mustermann schreibt", ("Max",), erlaubt=("Max Mustermann",)), [])

    def test_pfad_verbot(self):
        self.assertFalse(check.pfad_erlaubt("Website/content/de/erschliessung/az-1/index.md"))
        self.assertTrue(check.pfad_erlaubt("Hub-Entwicklung/erschliessung-entwurf/az-1.md"))


class Ordner(unittest.TestCase):
    def test_uebersicht_uebersprungen(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            for name in ("00-uebersicht.md", "README.md", "00-einleitung.md", "01-a.md"):
                open(os.path.join(d, name), "w").write("TITEL: x\n\ny")
            # nur die Übersichtsdatei und README werden übersprungen; 00-einleitung ist eine Seite
            self.assertEqual([f for f, _ in check.entwuerfe(d)], ["00-einleitung.md", "01-a.md"])

    def test_schnappschuss_namen(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "01-a.md"), "w").write("TITEL: x\nMEILENSTEIN: 1\nLABELS: Nachweis\n\nText #5")
            snap = os.path.join(d, "snap.jsonl")
            open(snap, "w").write('{"n": 5, "t": "Treffen mit Erika", "s": "open"}\n')
            befunde = check.pruefe("forgejo", d, snap, namen=(("Erika",), ()))
            self.assertTrue(any("snap.jsonl: name: Erika" in b for b in befunde), befunde)


class Projektsprache(unittest.TestCase):
    def test_findet_ap_und_m(self):
        self.assertEqual(check.find_projektsprache("siehe AP 4-5 und M30"), ["AP 4", "M30"])

    def test_hub_sprache_sauber(self):
        self.assertEqual(check.find_projektsprache("Sammlung filtern und einbetten"), [])


class Verweise(unittest.TestCase):
    def test_tote_verweise(self):
        self.assertEqual(check.find_tote_verweise("#844 und #9999", {844}), [9999])

    def test_nevent_laenge(self):
        self.assertEqual(check.find_kurze_nevents("https://gitworkshop.dev/nevent1qqsabc"), ["nevent1qqsabc"])


class Entwurf(unittest.TestCase):
    def test_parse_forgejo(self):
        e = check.parse_entwurf("TITEL: Nachweis\nMEILENSTEIN: 99\nLABELS: Nachweis, Community-Hub\n\nText")
        self.assertEqual((e["titel"], e["meilenstein"], e["labels"], e["body"]), ("Nachweis", 99, ["Nachweis", "Community-Hub"], "Text"))


if __name__ == "__main__":
    unittest.main()
