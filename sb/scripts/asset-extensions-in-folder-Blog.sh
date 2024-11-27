#welche Dateiendungen sind in den Markdown-Dateien in Verweisen enthalten:
grep -r -E '\.\w\w\w+\)' Blog/ | grep -v -E '\.html\)' \
| grep -v -E '\.de\)' | grep -v -E '\.org\)' | grep -v -E '\.nrw\)' \
| cut -d')' -f 1 | rev | cut -d'.' -f 1 | rev | sort -u

# jpeg
# jpg
# JPG
# mp4
# pdf
# png

# 1970520 => AKRK.md
# education => GwR-Tagung

# $grep -r -E '\.\w\w\w+\)' Blog/ | grep -v -E '\.html\)' | grep -v -E '\.de\)' | grep -v -E '\.org\)' | grep -v -E '\.nrw\)' | cut -d')' -f 1 | grep educa
# Blog/2024-09-17-GwR-Tagung.md:Unter dem spannenden Motto „...hier sollte eigentlich ein Titel stehen“ fand die diesjährige [GwR-Tagung](https://gwr.education

# $grep -r -E '\.\w\w\w+\)' Blog/ | grep -v -E '\.html\)' | grep -v -E '\.de\)' | grep -v -E '\.org\)' | grep -v -E '\.nrw\)' | cut -d')' -f 1 | grep 1970
# Blog/2024-10-02 AKRK.md:Wie OER insgesamt didaktische Prozesse verändern können und die Perspektive auf die Lernenden richten, beleuchtet auch die Forschung von [Eric Werth und Katherine Williams](https://doi.org/10.1080/02680513.2021.1970520

#welche Zeilen in Markdown Dateien enthalten "Asset"-Links,, die nicht in den Wordpress-Uploads vorhanden sind?
grep -r -E '\.\w\w\w+\)' Blog/ | grep -v -E '\.html\)' | grep -v -E '\.de\)' | grep -v -E '\.org\)' | grep -v -E '\.nrw\)' | cut -d')' -f 1 | grep -v 'oer\.comm'

# Kontrolliere, welche "Asset-Links" im aktuell zu übertragenden Blogpost vorhanden sind
grep -r -E '\.\w\w\w+\)' sb/content/ \
| grep -v -E '\.html\)' | grep -v -E '\.de\)' | grep -v -E '\.org\)' | grep -v -E '\.nrw\)' \
| cut -d')' -f 1 | grep -v 'oer\.comm' | grep -v hello-world \ #bereits übertragene Blogposts
| grep sdg-logo # aktuell zu übertragender Blogpost


#FIXME: #TODO: # es werden nur assets von oer.community heruntergeladen und z. B. nicht von pad.gwdg.de
  # Aufwand lohnt nicht, andere Assets (außerhalb unserer Wordpress-Instanz nur für jpeg/jpg, png, mp4
    #cat tmp-8JmqbYUnu/found-urls.txt | rev | cut -d\. -f1 | rev | nl | grep -v \/ >> tmp-8JmqbYUnu/vermeintlich-all-assets-urls.txt
    #cat tmp-8JmqbYUnu/vermeintlich-all-assets-urls.txt | grep -v 'md    ****' | cut -d'    ' -f 2 | sort -u | grep -v -E 'md|de|pdf|org|eu|html|education|1|1970|3601'
    #mp4: keine; #jpg: keine; #png: assets/images/blog/kemnitzer-tiktok.png; https://pad.gwdg.de/uploads