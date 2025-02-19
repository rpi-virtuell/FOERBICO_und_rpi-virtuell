/^###_tmpDate_:/ {
    linecontent = linecontent $0
}
/^#staticSiteGenerator:/ {
    $0 = $0 ORS "date: " linecontent
}
!/^###_tmpDate_:/