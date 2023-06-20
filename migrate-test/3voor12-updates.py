#!/usr/bin/env python3
import os

import elasticsearch


from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from dotenv import dotenv_values



config = dotenv_values(os.path.dirname(os.path.dirname(__file__)) + '/.env')

es = Elasticsearch("http://localhost:9210")

resp = helpers.scan(
    es,
    index="3voor12_updates", 
    scroll = '3m'
)

prepr_endpoint = config['PREPR_MIGRATE_ENDPOINT']

for num, doc in enumerate(resp):    
    print("%s" % str(doc))
    # TODO: Now post the update to prepr to create a bunch of content items

