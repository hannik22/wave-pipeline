import json
import os
import datetime
from wavedata import wavedata 
from watertemp import watertemp
from reportdata import reportdata 
from pymongo import MongoClient
import time

mongoSecret = os.getenv('MONGO_URI')

client = MongoClient(mongoSecret)

db = client['scheduler']

inputCollection  = db['subLocations']
cursor = inputCollection.find({})
inputResults = list(cursor)

for i in inputResults:
    endpoint = i['endPoint']
    city = i['name']
    lake = i['lake']
    reportId = i['reportId']
    urls = i['urls']
    try:
        outputcollection = db['waves']
        waves = wavedata(urls)
        report = reportdata(reportId)
        temp = watertemp(lake)
        mydict = {"endPoint": endpoint, "city": city, "lake":lake, "properties": waves, "last_modified": datetime.datetime.utcnow(), "report": report, "watertemp": temp}
        insert = outputcollection.replace_one({"city": city}, mydict, upsert=True)
        print('Mongo DB updated')
    except:
        print('Error fetching wave data!')