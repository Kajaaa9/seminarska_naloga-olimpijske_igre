import requests
import csv
import re


url = "https://www.olympics.com/en/olympic-games"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}


def shrani_url_kot_html():
    with open("oi5_olimpijske-igre.html", "w", encoding="utf-8") as f:
        f.write(requests.get(url, headers=headers).text)


def shrani_url_po_igrah():

    with open("oi5_olimpijske-igre.html", "r", encoding="utf-8") as f:
        url_html = f.read()

    vzorec = r'"@type":"ListItem",\s*"position":(\d+),\s*"url":"(https://www\.olympics\.com/olympic-games/([^"]+))"'

    matches = re.findall(vzorec, url_html, re.DOTALL)
    
    with open("oi6_url_po-igrah.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Zaporedna številka", "URL", "Mesto", "Leto"])
        
        for zap_st, full_url, mestoleto in matches:
            loceno = mestoleto.split('-')
            leto = loceno[-1]
            mesto = ' '.join(loceno[:-1]).title()
            
            writer.writerow([zap_st, full_url, mesto, leto])
