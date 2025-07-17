import requests
import csv
import re
import os


def st_medalj_po_drzavah():
    
    mapa = "oi7_html_po-igrah_medalje"
    os.mkdir("oi8_medalje_po_drzavah") #naredi novo mapo
    
    vzorec = r'<span data-cy="country-name" class="sc-26c0a561-6 kHkqQM"> ([^<]+)(?=<)</span></div><div data-cy="medal-module" data-medal-id="gold-medals-row-\d" title="Gold" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="medal-module" data-medal-id="silver-medals-row-72" title="Silver" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="medal-module" data-medal-id="bronze-medals-row-\d" title="Bronze" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><span class="mobile-hidden"></span><div data-cy="medal-module" data-medal-id="total-medals-row-\d" title="" class="Medal-styles__Wrapper-sc-645148e1-0 fEoULw"><span data-cy="medal-main" class="Medal-styles__Medal-sc-.{17}"><span data-cy="ocs-text-module" class="OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body">(-|\d+)</span></span></div><div data-cy="country-complete-name" data-row-id="country-medal-row-\d" class="sc-26c0a561-3 eWQUkL">'

    matches = re.findall(vzorec, url_html, re.DOTALL)

    for datoteka in os.listdir(mapa):
        pot = os.path.join(mapa, datoteka)
        with open(pot, "r", encoding="utf-8") as f: #odpre datoteko (iz mape oi7_html_po-igrah_medalje) in iz nje s pomocjo vzorca najde drzava, zlate, srebrne, bronaste, skupaj
            url_html = f.read()
            ime_datoteke = datoteka + "_medalje"
        
        with open(ime_datoteke, "w", newline="", encoding="utf-8") as datoteka_oi8: #ustvari datoteko za vsako leto posebaj znotraj mape oi8_medalje_po_drzavah
            writer = csv.writer(datoteka_oi8)
            writer.writerow(["Država", "Zlate medalje", "Srebrne medalje", "Bronaste medalje", "Skupaj"])
            
            for drzava, zlate, srebrne, bronaste, skupaj in matches:
                writer.writerow([drzava, zlate, srebrne, bronaste, skupaj])




#primer stare funkcije
def shrani_url_po_igrah():

    
    with open(ime_datoteke, "w", newline="", encoding="utf-8") as datoteka_oi8:
        writer = csv.writer(datoteka_oi8)
        writer.writerow(["Država", "Zlate medalje", "Srebrne medalje", "Bronaste medalje", "Skupaj"])
        
        for zap_st, full_url, mestoleto in matches:
            loceno = mestoleto.split('-')
            leto = loceno[-1]
            mesto = ' '.join(loceno[:-1]).title()
            url = full_url.replace("/olympic-games/", "/en/olympic-games/")
            
            writer.writerow([zap_st, url, mesto, leto])


def shrani_url_kot_html_po_igrah():
    
    os.mkdir("oi7_html_po-igrah")
    
    with open("oi6_url_po-igrah.csv", "r", encoding="utf-8") as datoteka_oi6:
        besedilo = csv.DictReader(datoteka_oi6)
        
        for vrstica in besedilo:
            url = vrstica["URL"]
            mesto = vrstica["Mesto"]
            leto = vrstica["Leto"]
            
            ime_datoteke = f"{leto}-{mesto.replace(' ', '_')}.html"
            pot = os.path.join("oi7_html_po-igrah", ime_datoteke)
                
            try:
                odziv = requests.get(url, headers=headers, timeout=10)
                odziv.raise_for_status()
                
                with open(pot, "w", encoding="utf-8") as izhodna_datoteka:
                    izhodna_datoteka.write(odziv.text)
                
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:   # ce pride do napake pri povezavi ali kaj v povezavi z requests
                print(f"Napaka pri dostopu do {url}: {str(e)}")

            except Exception as e:                              # ce pride do druge napake (npr. napaka pri zapisu v datoteko)
                print(f"Neznana napaka: {str(e)}")