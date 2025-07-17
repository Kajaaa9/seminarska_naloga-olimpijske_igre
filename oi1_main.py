import oi2_pridobi
import oi3_izlusci
import oi4_shrani
import os

if not os.path.exists("oi5_spletnastran.html"):     # shrani spletno stran kot html
    oi2_pridobi.shrani_url__kot_html()

if not os.path.exists("oi6_linki_po-igrah.csv"):    # shrani htmlje po igrah (letih) v csv
    oi2_pridobi.shrani_htmlje_po_igrah2()
