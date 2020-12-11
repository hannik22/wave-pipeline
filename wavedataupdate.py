
import requests
import json
import pandas as pd
import datetime
from validUrl import validUrl 

# mydict={}

# mapping = [
#     {'var': 'wvht', 'attribute': 'waveHeight', 'df': 'dwvht', 'rename': 'WaveHeight'},
#     {'var': 'wvpd', 'attribute': 'wavePeriod', 'df': 'dwvpd', 'rename': 'WavePeriod'},
#     {'var': 'wvdir', 'attribute': 'waveDirection', 'df': 'dwvdir', 'rename': 'WaveDirection'},
#     {'var': 'wnspd', 'attribute': 'windSpeed', 'df': 'dwnspd', 'rename': 'WindSpeed'},
#     {'var': 'wndir', 'attribute': 'windDirection', 'df': 'dwndir, 'rename': 'WindDirection'},
#     {'var': 'temp', 'attribute': 'temperature', 'df': dtemp, 'rename': 'Temperature'},
#     {'var': 'rainperc', 'attribute': 'probabilityOfPrecipitation', 'df': drainperc, 'rename': 'ChanceRain'},
# ]

def wavedata(url1, url2, url3):
    url = validUrl(url1, url2, url3)

    if url == 'Error':
        return {"ChanceRain": 0, "Temperature": 0, "WaveDirection": 0, "WaveHeight": 0, "WavePeriod": 0, "WindDirection": 0, "WindSpeed": 0, "validTime": 0}
    else:
        r = requests.get(url)
        x = r.json()

        ## wave height
        wvht = x['properties']['waveHeight']['values']
        dwvht = pd.json_normalize(wvht)[:]
        #format the time string
        dwvht['validTime'] = dwvht['validTime'].str[0:16]
        #format value
        dwvht['value'] = round((dwvht['value']*3.28084).astype(float), 1)
        #convert to date/time
        dwvht['validTime'] = pd.to_datetime(dwvht['validTime'], format = '%Y-%m-%dT%H:%M')
        #rename
        dwvht = dwvht.rename(columns = {"value": "WaveHeight"})
        print(dwvht)
        
        ##wave period
        wvpd = x['properties']['wavePeriod']['values']
        dwvpd = pd.json_normalize(wvpd)[:]
        #format the time string
        dwvpd['validTime'] = dwvpd['validTime'].str[0:16]
        #format value
        dwvpd['value'] = round(dwvpd['value'], 1)
        #convert to date/time
        dwvpd['validTime'] = pd.to_datetime(dwvpd['validTime'], format = '%Y-%m-%dT%H:%M')
        #rename
        dwvpd = dwvpd.rename(columns = {"value": "WavePeriod"})
        print(dwvpd)

            


wavedata('https://api.weather.gov/gridpoints/MKX/88,68', 'https://api.weather.gov/gridpoints/MKX/93,54', 'https://api.weather.gov/gridpoints/MKX/88,72')