import oi2_pridobi
import oi3_izlusci
import oi4_shrani
import os


if not os.path.exists("oi6.1_olimpijske-igre.html"):    # shrani spletno stran kot html
    oi2_pridobi.shrani_url_kot_html()                     # prenos spletne strani 18.7.2025

if not os.path.exists("oi6.2_url_po-igrah.csv"):        # shrani url-je posameznih iger v csv (iz html oi6.1)
    oi2_pridobi.shrani_url_po_igrah()

if not os.path.exists("oi7_html_po-igrah"):             # shrani html-je posameznih iger v mapo (iz url-jev v oi6.2)
    oi2_pridobi.shrani_url_kot_html_po_igrah()            # prenos spletnih strani 18.7.2025


if not os.path.exists("oi8.1_html_po-igrah_medalje"):   # shrani html-je za medalje posameznih iger v mapo (iz html oi6.1)
    oi2_pridobi.shrani_url_kot_html_po_igrah_medalje()    # prenos spletnih strani 18.7.2025

if not os.path.exists("oi8.2_medalje_po-igrah"):        # naredi mapo s csv tabelami medalj po drzavah za vsako igro posebaj (iz html-jev v mapi oi8.1)
    oi3_izlusci.st_medalj_po_drzavah()

if not os.path.exists("oi8.3_medalje_pregled.csv"):     # naredi eno csv tabelo medalj po letih (iz csv datotek v mapi oi8.2)
    oi4_shrani.medalje_skupaj()


if not os.path.exists("oi9.1_html_po-igrah_rezultati"): # shrani html-je za rezultate posameznih iger v mapo (iz html oi6.1)
    oi2_pridobi.shrani_url_kot_html_po_igrah_rezultati()  # prenos spletnih strani 18.7.2025

if not os.path.exists("oi9.2_discipline_po-igrah"):     # naredi mapo s csv tabelami disciplin po letih za vsako igro posebaj (iz html-jev v mapi oi9.1)
    oi3_izlusci.seznam_disciplin_po_letih()

if not os.path.exists("oi9.3_discipline_pregled.csv"):  # naredi eno csv tabelo disciplin po letih (iz csv datotek v mapi oi9.2)
    oi4_shrani.discipline_skupaj()