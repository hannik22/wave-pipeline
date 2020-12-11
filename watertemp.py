# coding: utf8

import requests
from bs4 import BeautifulSoup

def watertemp(lake):
    if lake == 'Lake Michigan':
        url = 'https://seatemperature.info/chicago-water-temperature.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tempblock = soup.find_all(class_='a27 a32 a20')[0].get_text()
        temp = tempblock.partition("C")[2]
        tempformat = temp.partition("°")[0]
        return tempformat
    else:
        url = 'https://seatemperature.info/duluth-water-temperature.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tempblock = soup.find_all(class_='a27 a32 a20')[0].get_text()
        temp = tempblock.partition("C")[2]
        tempformat = temp.partition("°")[0]
        return tempformat

        
