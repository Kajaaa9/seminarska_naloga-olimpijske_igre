import requests
import csv
import re
import os


def st_medalj_po_drzavah():

    vhodna_mapa = "oi7_html_po-igrah_medalje"
    os.mkdir("oi8_medalje_po_drzavah")
    
    vzorec = r'<span data-cy="country-name" class="sc-26c0a561-6 kHkqQM"> ([^<]+)(?=<)</span></div><div data-cy="medal-module" data-medal-id="gold-medals-row-\d" title="Gold" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="medal-module" data-medal-id="silver-medals-row-72" title="Silver" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="medal-module" data-medal-id="bronze-medals-row-\d" title="Bronze" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><span class="mobile-hidden"></span><div data-cy="medal-module" data-medal-id="total-medals-row-\d" title="" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="country-complete-name" data-row-id="country-medal-row-\d" class="sc-26c0a561-3 eWQUkL">'
    
    matches = re.findall(vzorec, url_html, re.DOTALL)

    for datoteka in os.listdir(vhodna_mapa):
        vhodna_pot = os.path.join(vhodna_mapa, datoteka)
        
        with open(vhodna_pot, "r", encoding="utf-8") as f: #odpre datoteko (iz mape oi7_html_po-igrah_medalje) in iz nje s pomocjo vzorca najde drzava, zlate, srebrne, bronaste, skupaj
            url_html = f.read()
                
        ime_datoteke = os.path.splitext(datoteka)[0] + "_medalje.csv"
        izhodna_pot = os.path.join("oi8_medalje_po_drzavah", ime_datoteke)      #ustvari datoteko za vsako leto posebaj znotraj mape oi8_medalje_po_drzavah
        
        with open(izhodna_pot, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Država", "Zlate medalje", "Srebrne medalje", "Bronaste medalje", "Skupaj"])
            
            for drzava, zlate, srebrne, bronaste, skupaj in matches:
                writer.writerow([drzava, zlate, srebrne, bronaste, skupaj])
            # for match in matches:
            #     # Če je število medalj '-' (ni podatka), zamenjaj z 0
            #     podatki = [m.strip() if m != '-' else '0' for m in match]
            #     writer.writerow(podatki)
        
        print(f"Uspešno ustvarjeno: {ime_datoteke}")

