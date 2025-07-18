import oi2_pridobi
import oi3_izlusci
import oi4_shrani
import os

if not os.path.exists("oi5_olimpijske-igre.html"):      # shrani spletno stran kot html
    oi2_pridobi.shrani_url_kot_html()                     # prenos spletne strani 18.7.2025

if not os.path.exists("oi6_url_po-igrah.csv"):          # shrani url-je po igrah (letih) v csv
    oi2_pridobi.shrani_url_po_igrah()                     # prenos spletne strani 18.7.2025

if not os.path.exists("oi7_html_po-igrah"):             # shrani html-je po igrah (letih) v mapo
    oi2_pridobi.shrani_url_kot_html_po_igrah()            # prenos spletnih strani 18.7.2025

if not os.path.exists("oi7_html_po-igrah_medalje"):     # shrani html-je za medalje po igrah (letih) v mapo
    oi2_pridobi.shrani_url_kot_html_po_igrah_medalje()    # prenos spletnih strani 18.7.2025

if not os.path.exists("oi8_medalje_po_drzavah"):        # naredi mapo s csv tabelami medalj po drzavah (za vsako igro (leto) posebaj)
    oi3_izlusci.st_medalj_po_drzavah()

if not os.path.exists("oi7_html_po-igrah_rezultati"):   # shrani html-je za rezultate po igrah (letih) v mapo
    oi2_pridobi.shrani_url_kot_html_po_igrah_rezultati()  # prenos spletnih strani 18.7.2025

if not os.path.exists("oi9_discipline_po-igrah"):       # naredi mapo s csv tabelami disciplin po letih
    oi3_izlusci.seznam_disciplin_po_letih()

