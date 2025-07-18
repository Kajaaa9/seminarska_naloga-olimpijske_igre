import requests
import csv
import re
import os


def st_medalj_po_drzavah():

    vhodna_mapa = "oi7_html_po-igrah_medalje"
    os.mkdir("oi8_medalje_po_drzavah")
    
    vzorec = re.compile(
        r'<span data-cy="country-name"[^>]*>([^<]+)</span>.*?' # drzava
        r'<div data-cy="medal-module"[^>]*data-medal-id="gold-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?' # zlate
        r'<div data-cy="medal-module"[^>]*data-medal-id="silver-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?' # srebrne
        r'<div data-cy="medal-module"[^>]*data-medal-id="bronze-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?' # bronaste
        r'<div data-cy="medal-module"[^>]*data-medal-id="total-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>', # skupaj
        re.DOTALL)    

    for datoteka in os.listdir(vhodna_mapa):
        vhodna_pot = os.path.join(vhodna_mapa, datoteka)
        
        with open(vhodna_pot, "r", encoding="utf-8") as f: #odpre datoteko (iz mape oi7_html_po-igrah_medalje) in iz nje s pomocjo vzorca najde drzava, zlate, srebrne, bronaste, skupaj
            url_html = f.read()

        matches = vzorec.findall(url_html)

        ime_datoteke = os.path.splitext(datoteka)[0] + "_medalje.csv"
        izhodna_pot = os.path.join("oi8_medalje_po_drzavah", ime_datoteke)      #ustvari datoteko za vsako leto posebaj znotraj mape oi8_medalje_po_drzavah
        
        with open(izhodna_pot, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Država", "Zlate medalje", "Srebrne medalje", "Bronaste medalje", "Skupaj"])
            
            for drzava, zlate, srebrne, bronaste, skupaj in matches:
                drzava = drzava.replace("&#x27;", "'")
                medalje = [zlate, srebrne, bronaste, skupaj]
                medalje = [m if m != '-' else '0' for m in medalje]
                writer.writerow([drzava] + medalje)
        
    print(f"Datoteka {ime_datoteke} ustvarjena.")

