import json
import datetime
from wavedata import wavedata 
from watertemp import watertemp
from reportdata import reportdata 
from pymongo import MongoClient
import time

client = MongoClient('mongodb+srv://khannigan:91summon@cluster0.tnv2i.gcp.mongodb.net/test')

def seed_mongo(endpoint, city, lake, url1, url2, url3, report):
    try:
        db = client['scheduler']
        collection = db['waves']
        waves = wavedata(url1, url2, url3)
        report = reportdata(report)
        temp = watertemp(lake)
        mydict = {"endPoint": endpoint, "city": city, "lake":lake, "properties": waves, "last_modified": datetime.datetime.utcnow(), "report": report, "watertemp": temp}
        insert = collection.replace_one({"city": city}, mydict)
        print('Mongo DB updated')
    except:
        print('Error fetching wave data!')


if __name__ == "__main__":
    seed_mongo('Milwaukee', 'Milwaukee, WI', 'Lake Michigan', 'https://api.weather.gov/gridpoints/MKX/88,68', 'https://api.weather.gov/gridpoints/MKX/93,54', 'https://api.weather.gov/gridpoints/MKX/88,72', 'LMZ644')
    seed_mongo('Chicago', 'Chicago, IL', 'Lake Michigan', 'https://api.weather.gov/gridpoints/LOT/74,77', 'https://api.weather.gov/gridpoints/LOT/73,80', 'https://api.weather.gov/gridpoints/LOT/76,76', 'LMZ741')
    seed_mongo('Sheboygan', 'Sheboygan, WI', 'Lake Michigan', 'https://api.weather.gov/gridpoints/MKX/93,96', 'https://api.weather.gov/gridpoints/MKX/93,98', 'https://api.weather.gov/gridpoints/MKX/93,101', 'LMZ643')
    seed_mongo('DoorCounty', 'Door County, WI', 'Lake Michigan',  'https://api.weather.gov/gridpoints/GRB/105,51', 'https://api.weather.gov/gridpoints/GRB/109,59', 'https://api.weather.gov/gridpoints/GRB/115,73', 'LMZ541')
    seed_mongo('MichiganCity', 'Michigan City, IN', 'Lake Michigan',  'https://api.weather.gov/gridpoints/IWX/6,63', 'https://api.weather.gov/gridpoints/LOT/99,66', 'https://api.weather.gov/gridpoints/IWX/7,64', 'LMZ046')
    seed_mongo('SaintJoseph', 'Saint Joseph, MI', 'Lake Michigan',  'https://api.weather.gov/gridpoints/GRR/15,6', 'https://api.weather.gov/gridpoints/IWX/18,80', 'https://api.weather.gov/gridpoints/IWX/18,79', 'LMZ046')
    seed_mongo('Holland', 'Holland, MI', 'Lake Michigan',  'https://api.weather.gov/gridpoints/GRR/22,37', 'https://api.weather.gov/gridpoints/GRR/22,31', 'https://api.weather.gov/gridpoints/GRR/21,45', 'LMZ046')
    seed_mongo('Marquette', 'Marquette, MI', 'Lake Superior',  'https://api.weather.gov/gridpoints/MQT/158,69', 'https://api.weather.gov/gridpoints/MQT/152,75', 'https://api.weather.gov/gridpoints/MQT/154,70', 'LSZ263')
    seed_mongo('Duluth', 'Duluth, MN', 'Lake Superior',  'https://api.weather.gov/gridpoints/MQT/158,69', 'https://api.weather.gov/gridpoints/MQT/152,75', 'https://api.weather.gov/gridpoints/MQT/154,70', 'LMZ046')