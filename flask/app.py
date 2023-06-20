import logging
import os
from datetime import datetime
from zoneinfo import ZoneInfo
import locale
locale.setlocale(locale.LC_ALL, 'nl_NL')

import requests
from dotenv import dotenv_values
from flask import Flask, render_template


app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
config = dotenv_values(os.path.dirname(os.path.dirname(__file__)) + '/.env')
model = "e1cc318d-6b70-413d-8797-b438734fd19d"

def get_by_uuid(uuid):
    return get({})


def get(query):
    response = requests.post(
    config['PREPR_ENDPOINT'],
    headers =  {
            'Content-Type': 'application/json'
    },
    json={'query':query}
    )
    return response.json()

def inspect():
    json = get("""query {
   __type(name:"Drievoor12update") {
      fields {
         name
         description
      }  
   }}
   """)
    return json


@app.route('/')
def index():
    json = get("""query  listall {
      Drievoor12updates(limit: 30, sort: changed_on_DESC) {    
        items {
          _id
          id
          title  
          subtitle
        }
      }
    }
    """)
  #  logging.info(inspect())
    return render_template('index.html', updates=json['data']['Drievoor12updates']['items'])

@app.route('/<path:uuid>')
def update(uuid):
    json = get("""query  {
      Drievoor12updates(where: {id:"%s"}) {
        items {
          id
          title  
          subtitle
          text   
          _publish_on 
        }
      }
    }
    """ % uuid)
    return render_template('update.html', update=json['data']['Drievoor12updates']['items'][0])


@app.template_filter('datetime')
def _jinja2_filter_datetime(date):
    date = datetime.fromisoformat(date)
    native = date.replace(tzinfo=ZoneInfo('Europe/Amsterdam'))
    return native.strftime('%d %B, %Y') 

if __name__ == "__main__":
    app.run(debug=True)
