import csv
import os

def medalje_skupaj():

    podatki_medalj = {}  # slovar {drzava: {letomestovrsta: [zlate, srebrne, bronaste, skupaj]}}
    igre = []  # seznam leto-mesto-vrsta, po vrstnem redu datotek

    for datoteka in os.listdir("oi8.2_medalje_po_drzavah"):
        letomestovrsta = datoteka.replace("_medalje.csv", "")
        igre.append(letomestovrsta)
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

                podatki_medalj[drzava][letomestovrsta] = [zlate, srebrne, bronaste, skupaj]

    vse_drzave = sorted(podatki_medalj.keys())

    with open("oi8.3_medalje_pregled.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        glava = ["Država"]
        for igra in igre:
            glava += [f"{igra}-Zlate", f"{igra}-Srebrne", f"{igra}-Bronaste", f"{igra}-Skupaj"]
        writer.writerow(glava)

        for drzava in vse_drzave:
            vrstica = [drzava]
            for igra in igre:
                medalje = podatki_medalj[drzava].get(igra, [0, 0, 0, 0])
                vrstica.extend(medalje)
            writer.writerow(vrstica)

    print("Datoteka oi8.3_medalje_pregled.csv ustvarjena.")


def discipline_skupaj():

    igre = []
    vse_discipline = set()
    discipline_po_igrah = {}  # slovar: {letomestovrsta: množica_disciplin}

    for datoteka in os.listdir("oi9.2_discipline_po-igrah"):
        letomestovrsta = datoteka.replace("_discipline.csv", "")
        igre.append(letomestovrsta)
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

            discipline_po_igrah[letomestovrsta] = discipline

    vse_discipline = sorted(vse_discipline) # po abecedi

    with open("oi9.3_discipline_pregled.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        glava = ["Disciplina"] + igre
        writer.writerow(glava)

        # vrstica_vrsta = ["Vrsta"] + [podatki_igre.get(igra) for igra in igre]

        # writer.writerow(vrstica_vrsta)

        for disciplina in vse_discipline:
            vrstica = [disciplina]  # začnemo z imenom discipline

            for igra in igre:
                if disciplina in discipline_po_igrah.get(igra, set()):
                    vrstica.append("1")
                else:
                    vrstica.append("0")
            writer.writerow(vrstica)  # zapišemo vrstico v datoteko

    print("Datoteka oi9.3_discipline_pregled.csv ustvarjena.")

