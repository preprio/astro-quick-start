#!/usr/bin/env python3
import os

import requests
from elasticsearch import Elasticsearch, helpers
from dotenv import dotenv_values


config = dotenv_values(os.path.dirname(os.path.dirname(__file__)) + '/.env')
model = "e1cc318d-6b70-413d-8797-b438734fd19d"

headers={
    'Authorization':  'Bearer ' + config['PREPR_MIGRATE_TOKEN']
}

def get_by_mgnl_uuid(uuid):
    response = requests.get("https://api.eu1.prepr.io/content_items?items[nl-NL][id][body][eq]=" + uuid + "&fields=created_by,title,items,id,tags&model[id]=" + model,
         headers= headers,                             
         )
    if response.status_code == 200:
        items =  response.json()["items"]
        if len(items) > 0:
            return items[0]
        else:
            return None
    else:
        return None
    
def to_json(value):
    if isinstance(value, list):
        return {
            "items": list(map(lambda v: to_json(v), filter(lambda v: v != '', value)))
        }
    if isinstance(value, str):
        return {
            "body": value
        }
    if isinstance(value, bool):
        return {
            "value": value
        }
    raise Exception("Unknown type: " + str(type(value)))

def post_to_prepr(fields, original):
    incoming_uuid = fields['id']
    result = get_by_mgnl_uuid(incoming_uuid)
    uuid = result['id'] if result else None
    json = {
          "locales": [ "nl-NL"],
           "model": {
             "id": model
           },
           "status": {
              "nl-NL": {
                "body": "Done"
             }
           },
          "publish_on": {
             "nl-NL": original['publishDate'] / 1000
           },
           "items": {
               "nl-NL": {        
                 
               }
           }
    }
    for key in fields:      
        json['items']['nl-NL'][key] = to_json(fields[key])

        
    response = requests.post("https://api.eu1.prepr.io/content_items/" +(uuid if uuid else ""),
       headers= headers,
       json= json
    )
    if response.status_code >= 200 and response.status_code < 300:
        print(response.status_code)
        print(response.json())
        return
    else: 
        raise Exception("Error posting to Prepr: " + str(response.status_code) + " " + response.text)



def map_to_prepr(source):
    return {
        'id': source['id'],
        'title': source['title'],
        'slug': source['id'],
        'subtitle': source['subtitle'], 
        'highlighted': source['highlighted'], 
        'text': source['text'],
        'tags': source['tags'] # doesn't work?

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
        print(num)
        post_to_prepr(map_to_prepr(source), source)
        if num > 100:
            # just testing. 100 should be enough
            break
    




migrate()