/^###_tmpAuthor_:/ {
    linecontent = linecontent ORS $0
}
/^#staticSiteGenerator:/ {
    $0 = $0 ORS "author:" linecontent
}
!/^###_tmpAuthor_:/