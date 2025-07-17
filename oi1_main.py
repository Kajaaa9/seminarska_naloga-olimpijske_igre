import oi2_pridobi
import oi3_izlusci
import oi4_shrani
import os

if not os.path.exists("oi5_olimpijske-igre.html"):     # shrani spletno stran kot html
    oi2_pridobi.shrani_url_kot_html()

if not os.path.exists("oi6_url_po-igrah.csv"):    # shrani htmlje po igrah (letih) v csv
    oi2_pridobi.shrani_url_po_igrah()
