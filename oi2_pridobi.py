import requests
import csv
import re
import os
import time

url = "https://www.olympics.com/en/olympic-games"   # prenos spletne strani 17.7.2025
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}


def shrani_url_kot_html():
    with open("oi6.1_olimpijske-igre.html", "w", encoding="utf-8") as f:
        f.write(requests.get(url, headers=headers).text)
    print("Datoteka oi6.1_olimpijske-igre.html ustvarjena.")


def shrani_url_po_igrah():

    with open("oi6.1_olimpijske-igre.html", "r", encoding="utf-8") as f:
        url_html = f.read()

    vzorec = r'"@type":"ListItem",\s*"position":(\d+),\s*"url":"(https://www\.olympics\.com/olympic-games/([^"]+))"'
    matches = re.findall(vzorec, url_html, re.DOTALL)

    vzorec2 = r'"slug":"([^"]+?)".*?"season":"(Summer|Winter)"'
    matches2 = dict(re.findall(vzorec2, url_html))
    
    with open("oi6.2_url_po-igrah.csv", "w", newline="", encoding="utf-8") as datoteka_oi5:
        writer = csv.writer(datoteka_oi5)
        writer.writerow(["Zaporedna številka", "URL", "Mesto", "Leto", "Vrsta"])
        
        for zap_st, full_url, mestoleto in matches:
            loceno = mestoleto.split('-')
            leto = loceno[-1]
            mesto = ' '.join(loceno[:-1]).title()
            url = full_url.replace("/olympic-games/", "/en/olympic-games/")
            vrsta = matches2.get(mestoleto.lower(), "Neznano")

            if int(leto) > 2024:              # da pridobim url-je le za olimpijske igre, ki so ze potekale
                continue

            writer.writerow([zap_st, url, mesto, leto, vrsta])

    print("Datoteka oi6.2_url_po-igrah.csv ustvarjena.")


def shrani_url_kot_html_po_igrah():
    
    os.mkdir("oi7_html_po-igrah")
    
    with open("oi6.2_url_po-igrah.csv", "r", encoding="utf-8") as datoteka_oi6:
        besedilo = csv.DictReader(datoteka_oi6)
        
        for vrstica in besedilo:
            url = vrstica["URL"]
            mesto = vrstica["Mesto"]
            leto = vrstica["Leto"]
            
            ime_datoteke = f"{leto}-{mesto.replace(' ', '_')}.html"
            polna_pot = os.path.join("oi7_html_po-igrah", ime_datoteke)
                
            try:
                odziv = requests.get(url, headers=headers, timeout=10)
                odziv.raise_for_status()
                
                with open(polna_pot, "w", encoding="utf-8") as izhodna_datoteka:
                    izhodna_datoteka.write(odziv.text)
                
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"Napaka pri dostopu do {url}: {str(e)}")

            except Exception as e:
                print(f"Neznana napaka: {str(e)}")

    print("Mapa oi7_html_po-igrah ustvarjena.")


def shrani_url_kot_html_po_igrah_medalje():
    
    os.mkdir("oi8.1_html_po-igrah_medalje")
    
    with open("oi6.2_url_po-igrah.csv", "r", encoding="utf-8") as datoteka_oi6:
        besedilo = csv.DictReader(datoteka_oi6)
        
        for vrstica in besedilo:
            url = vrstica["URL"] + "/medals"
            mesto = vrstica["Mesto"]
            leto = vrstica["Leto"]
            vrsta = vrstica["Vrsta"]
            
            ime_datoteke = f"{leto}-{mesto.replace(' ', '_')}-{vrsta}.html"
            polna_pot = os.path.join("oi8.1_html_po-igrah_medalje", ime_datoteke)
                
            try:
                odziv = requests.get(url, headers=headers, timeout=10)
                odziv.raise_for_status()
                
                with open(polna_pot, "w", encoding="utf-8") as izhodna_datoteka:
                    izhodna_datoteka.write(odziv.text)
                
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"Napaka pri dostopu do {url}: {str(e)}")
            except Exception as e:
                print(f"Neznana napaka: {str(e)}")

    print("Mapa oi8.1_html_po-igrah_medalje ustvarjena.")


def shrani_url_kot_html_po_igrah_rezultati():
    
    os.mkdir("oi9.1_html_po-igrah_rezultati")
    
    with open("oi6.2_url_po-igrah.csv", "r", encoding="utf-8") as datoteka_oi6:
        besedilo = csv.DictReader(datoteka_oi6)
        
        for vrstica in besedilo:
            url = vrstica["URL"] + "/results"
            mesto = vrstica["Mesto"]
            leto = vrstica["Leto"]
            vrsta = vrstica["Vrsta"]

            ime_datoteke = f"{leto}-{mesto.replace(' ', '_')}-{vrsta}.html"
            polna_pot = os.path.join("oi9.1_html_po-igrah_rezultati", ime_datoteke)
                
            try:
                odziv = requests.get(url, headers=headers, timeout=10)
                odziv.raise_for_status()
                
                with open(polna_pot, "w", encoding="utf-8") as izhodna_datoteka:
                    izhodna_datoteka.write(odziv.text)
                
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"Napaka pri dostopu do {url}: {str(e)}")
            except Exception as e:
                print(f"Neznana napaka: {str(e)}")

    print("Mapa oi9.1_html_po-igrah_rezultati ustvarjena.")

