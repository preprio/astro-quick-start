#!/usr/bin/env python3
import os

import requests
from elasticsearch import Elasticsearch, helpers
from dotenv import dotenv_values


config = dotenv_values(os.path.dirname(os.path.dirname(__file__)) + '/.env')
def post_to_prepr(fields):
    token = config['PREPR_MIGRATE_TOKEN']
    response = requests.post("https://api.eu1.prepr.io/content_items",
       headers={
              'Authorization':  'Bearer ' + token
       },
       json={
           "locales": [ "nl-NL"],
           "model": {
             "id": "e1cc318d-6b70-413d-8797-b438734fd19d"
           },
           "status": {
              "nl-NL": {
                "body": "Done"
             }
           },
          "publish_on": {
             "nl-NL": 1600262640
           },
           "items": {
               "nl-NL": {        
                   "title": {
                      "body": fields['title']
                  },
                  "mgnl_uuid": {
                      "body": fields['id'][0:20]
                  }
               }
           }
       }
    )
    if response.status_code == 201:
        print(response.status_code)
        print(response.json())
        return
    else: 
        raise Exception("Error posting to Prepr: " + str(response.status_code) + " " + response.text)



def map_to_prepr(source):
    return {
        'id': source['id'],
        'title': source['title'], 
        'text': source['text']
    }

def migrate():
    es = Elasticsearch("http://localhost:9210")

    resp = helpers.scan(
      es,
      index="3voor12_updates", 
      scroll = '3m'
    )



    for num, doc in enumerate(resp):    
        print("%s" % str(doc))
        source = doc["_source"]    
        post_to_prepr(map_to_prepr(source))            




migrate()