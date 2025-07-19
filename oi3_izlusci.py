import csv
import re
import os


def st_medalj_po_drzavah():

    vhodna_mapa = "oi8.1_html_po-igrah_medalje"
    os.mkdir("oi8.2_medalje_po_drzavah")
    
    vzorec = re.compile(
        r'<span data-cy="country-name"[^>]*>([^<]+)</span>.*?'
        r'<div data-cy="medal-module"[^>]*data-medal-id="gold-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?'
        r'<div data-cy="medal-module"[^>]*data-medal-id="silver-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?'
        r'<div data-cy="medal-module"[^>]*data-medal-id="bronze-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>.*?'
        r'<div data-cy="medal-module"[^>]*data-medal-id="total-medals-row-\d+".*?>'
        r'.*?<span data-cy="ocs-text-module"[^>]*>(\d+|-)</span>',
        re.DOTALL)

    for datoteka in os.listdir(vhodna_mapa):
        vhodna_pot = os.path.join(vhodna_mapa, datoteka)
        
        with open(vhodna_pot, "r", encoding="utf-8") as f:
            url_html = f.read()

        matches = vzorec.findall(url_html)

        podatki = []
        for drzava, zlate, srebrne, bronaste, skupaj in matches:
            drzava = drzava.replace("&#x27;", "'")
            medalje = [zlate, srebrne, bronaste, skupaj]
            medalje = [m if m != '-' else '0' for m in medalje]
            podatki.append([drzava] + medalje)

        podatki.sort(key=lambda x: x[0])  # urejanje po abecedi

        ime_datoteke = os.path.splitext(datoteka)[0] + "_medalje.csv"
        izhodna_pot = os.path.join("oi8.2_medalje_po_drzavah", ime_datoteke)      #ustvari datoteko za vsako leto posebaj znotraj mape oi8.2_medalje_po_drzavah
        
        with open(izhodna_pot, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Država", "Zlate medalje", "Srebrne medalje", "Bronaste medalje", "Skupaj"])
            writer.writerows(podatki)
        
    print("Mapa oi8.2_medalje_po_drzavah ustvarjena.")


def seznam_disciplin_po_letih():

    vhodna_mapa = "oi9.1_html_po-igrah_rezultati"
    os.mkdir("oi9.2_discipline_po-igrah")
        
    vzorec = r'"sportDisciplineId":"[^"]+?".*?"title":"([^"]+?)"'

    for datoteka in os.listdir(vhodna_mapa):

        vhodna_pot = os.path.join(vhodna_mapa, datoteka)

        with open(vhodna_pot, "r", encoding="utf-8") as f:
            url_html = f.read()

        matches = re.findall(vzorec, url_html, re.DOTALL)

        matches = sorted(matches)

        ime_datoteke = os.path.splitext(datoteka)[0] + "_discipline.csv"
        izhodna_pot = os.path.join("oi9.2_discipline_po-igrah", ime_datoteke)
        
        with open(izhodna_pot, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Disciplina"])
            
            for disciplina in matches:
                writer.writerow([disciplina])
        
    print("Mapa oi9.2_discipline_po-igrah ustvarjena.")

