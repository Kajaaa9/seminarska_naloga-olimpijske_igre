import requests
import csv
import re


url = "https://www.olympics.com/en/olympic-games"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}


def shrani_url__kot_html():
    with open("oi5_spletnastran.html", "w", encoding="utf-8") as f:
        f.write(requests.get(url, headers=headers).text)


def shrani_htmlje_po_igrah2():

    with open("oi5_spletnastran.html", "r", encoding="utf-8") as f:
        url_html = f.read()

    vzorec = r'"@type":"ListItem",\s*"position":(\d+),\s*"url":"(https://www\.olympics\.com/olympic-games/([^"]+))"'

    matches = re.findall(vzorec, url_html, re.DOTALL)
    
    with open("oi6_linki_po-igrah.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Zaporedna številka", "URL", "Mesto-Leto"])  # Trije stolpci
        for poz, url, mestoleto in matches:
            writer.writerow([poz, url, mestoleto])
