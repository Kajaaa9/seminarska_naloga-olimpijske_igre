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
        
    print("Mapa oi8_medalje_po_drzavah ustvarjena.")


def seznam_disciplin_po_letih():

    vhodna_mapa = "oi7_html_po-igrah_rezultati"
    os.mkdir("oi9_discipline_po-igrah")
        
    vzorec = r'"sportDisciplineId":"[^"]+?".*?"title":"([^"]+?)"'

    for datoteka in os.listdir(vhodna_mapa):

        vhodna_pot = os.path.join(vhodna_mapa, datoteka)

        with open(vhodna_pot, "r", encoding="utf-8") as f:
            url_html = f.read()

        matches = re.findall(vzorec, url_html, re.DOTALL)

        ime_datoteke = os.path.splitext(datoteka)[0] + "_discipline.csv"
        izhodna_pot = os.path.join("oi9_discipline_po-igrah", ime_datoteke)
        
        with open(izhodna_pot, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Disciplina"])
            
            for disciplina in matches:
                writer.writerow([disciplina])
        
    print("Mapa oi9_discipline_po-igrah ustvarjena.")


def discipline_skupaj():
    
    podatki_igre = {}
    with open("oi6_url_po-igrah.csv", "r", encoding="utf-8") as f:
        besedilo = csv.DictReader(f)
        for vrstica in besedilo:

            leto = vrstica["Leto"]
            mesto = vrstica["Mesto"].replace(" ", "_")
            ime = f"{leto}-{mesto}"

            vrsta = vrstica["Vrsta"]
            podatki_igre[ime] = vrsta #slovar z {letomesto:vrsta}


    igre = []  # to bo v glavi tabele
    vse_discipline = set()
    discipline_po_igrah = {}  # slovar: {letomesto: množica_disciplin}

    for datoteka in os.listdir("oi9_discipline_po-igrah"):
        letomesto = datoteka.replace("_discipline.csv", "")
        igre.append(letomesto)
        pot = os.path.join("oi9_discipline_po-igrah", datoteka)

        with open(pot, "r", encoding="utf-8") as f:
            besedilo = csv.reader(f)
            next(besedilo)  # preskoci glavo
            discipline = set()  # lokalna množica disciplin za to igro
            for vrstica in besedilo:
                disciplina = vrstica[0]
                # disciplina = vrstica[0].strip()  # odstrani presledke....to bom dala samo ce bo nujno

                if disciplina:  # ce ni prazno-zaradi zadnje vrstice
                    discipline.add(disciplina) 
                    vse_discipline.add(disciplina)

            discipline_po_igrah[letomesto] = discipline

    vse_discipline = sorted(vse_discipline) # po abecedi

    with open("oi10_discipline_pregled.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        glava = ["Disciplina"] + igre
        writer.writerow(glava)

        vrstica_vrsta = ["Vrsta"] + [podatki_igre.get(igra) for igra in igre]

        writer.writerow(vrstica_vrsta)

        for disciplina in vse_discipline:
            vrstica = [disciplina]  # začnemo z imenom discipline

            for igra in igre:
                if disciplina in discipline_po_igrah.get(igra, set()):
                    vrstica.append("X")
                else:
                    vrstica.append("-")
            writer.writerow(vrstica)  # zapišemo vrstico v datoteko

    print("Datoteka oi10_discipline_pregled.csv ustvarjena.")

