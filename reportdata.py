import requests
import json
from bs4 import BeautifulSoup

def reportdata(url):
    page = requests.get('https://forecast.weather.gov/shmrn.php?mz='+url)
    soup = BeautifulSoup(page.text, 'html.parser')
    headers =[]
    bodies = []
    for tag in soup.find_all("strong"):
        headers.append(tag.get_text(strip=True))
    for tag in soup.find_all("strong"):
        bodies.append(tag.next_sibling.replace("\n\u00a0"," ").replace("\n\n"," ").replace("$$\n",""))

    content = [{"header":h, "body": b} for h, b in zip(headers, bodies)]

    return content