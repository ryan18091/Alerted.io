import pyowm
import sqlite3
from time import sleep
from datetime import time
import json
import pickle
from time import sleep

owm = pyowm.OWM('73a7404557976550084f91273468669d')

conn = sqlite3.connect('OWMdata.db')
c = conn.cursor()

def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS ZipcodeWeather(Zipcode INT, Weather BLOB)')

create_tables()

country_code = 'us'
#Country Codes http://sustainablesources.com/resources/country-abbreviations/

with open("zipcodes.txt", 'rb') as fp:
    b = pickle.load(fp)


class OWNquery(object):

    def __init__(self, zipcode, country_code):
        self.zipcode = zipcode
        self.country_code = country_code

    def query(self):
        LocalWeather = owm.weather_at_zip_code(str(self.zipcode), str(self.country_code))
        return LocalWeather

for zipcode in b:

    sleep(1)
    country_code = 'us'
    try:

        OWNqueryINST = OWNquery(zipcode, country_code)
        OWMWeatherObject = (OWNqueryINST.query()).get_weather()

        c.execute('SELECT Zipcode from ZipcodeWeather')
        zipcodeList = (i for i in c.fetchall())

        m = OWMWeatherObject.to_JSON()
        JsonWeather = json.loads(m)

        JsonSTR = str(JsonWeather)

        if zipcode in zipcodeList:
            c.execute('UPDATE ZipcodeWeather SET Weather = ? WHERE Zipcode = ?', (JsonWeather, zipcode))
            conn.commit()


        else:
            c.execute('INSERT INTO ZipcodeWeather VALUES (?,?)', (zipcode, JsonSTR))
            conn.commit()

    except Exception as e:
        print(e, zipcode)









