import csv
import os

def medalje_skupaj():
    
    podatki_igre = {}
    with open("oi6_url_po-igrah.csv", "r", encoding="utf-8") as f:
        besedilo = csv.DictReader(f)
        for vrstica in besedilo:
            leto = vrstica["Leto"]
            mesto = vrstica["Mesto"].replace(" ", "_")
            ime = f"{leto}-{mesto}"
            vrsta = vrstica["Vrsta"]
            podatki_igre[ime] = vrsta

    podatki_medalj = {}  # slovar: {drzava: {letomesto: [zlate, srebrne, bronaste, skupaj]}}
    igre = []  # seznam let-mest, po vrstnem redu datotek

    for datoteka in os.listdir("oi8.2_medalje_po_drzavah"):
        letomesto = datoteka.replace("_medalje.csv", "")
        igre.append(letomesto)
        pot = os.path.join("oi8.2_medalje_po_drzavah", datoteka)

        with open(pot, "r", encoding="utf-8") as f:
            besedilo = csv.DictReader(f)

            for vrstica in besedilo:
                drzava = vrstica["Država"]
                zlate = int(vrstica["Zlate medalje"])
                srebrne = int(vrstica["Srebrne medalje"])
                bronaste = int(vrstica["Bronaste medalje"])
                skupaj = int(vrstica["Skupaj"])

                if drzava not in podatki_medalj:
                    podatki_medalj[drzava] = {}

                podatki_medalj[drzava][letomesto] = [zlate, srebrne, bronaste, skupaj]

    vse_drzave = sorted(podatki_medalj.keys())

    # Priprava glave tabele z 4 stolpci za vsak letomesto
    glava = ["Država"]
    for igra in igre:
        glava += [f"{igra}-Zlate", f"{igra}-Srebrne", f"{igra}-Bronaste", f"{igra}-Skupaj"]

    with open("oi8.3_medalje_pregled.csv", "w", newline="", encoding="utf-8") as f:
        pisalec = csv.writer(f)
        pisalec.writerow(glava)

        for drzava in vse_drzave:
            vrstica = [drzava]
            for igra in igre:
                medalje = podatki_medalj[drzava].get(igra, [0, 0, 0, 0])
                vrstica.extend(medalje)
            pisalec.writerow(vrstica)

    print("Datoteka oi8.3_medalje_pregled.csv ustvarjena.")


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

    for datoteka in os.listdir("oi9.2_discipline_po-igrah"):
        letomesto = datoteka.replace("_discipline.csv", "")
        igre.append(letomesto)
        pot = os.path.join("oi9.2_discipline_po-igrah", datoteka)

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

    with open("oi9.3_discipline_pregled.csv", "w", newline="", encoding="utf-8") as f:
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

    print("Datoteka oi9.3_discipline_pregled.csv ustvarjena.")

