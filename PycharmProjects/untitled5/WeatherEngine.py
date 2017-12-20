# a93323883be13012

import urllib.request
import json
import sqlite3

import ast
from WeatherFunctions import newZipcode
from time import sleep

#-999 = a null value
#A basic conversion of precipitation to snow can be used to obtain an approximate snow reading. If snow precipitation
# is listed as e.g. 0.05 inches, this is water equivalent. Multiply by about 12 to get snow in inches. In the above
# example, 0.05 x 12 = 0.6 inches of snow. Dry, fluffy snow has much less water in it, and one should use a conversion
#  factor of about 20 instead.

#
# sleep(3600)
from UserZipcodes import zipcodes

#fetches weather data through weather underground api and inserts it into the db
for zipcode in zipcodes:

    #create a list of currently tracked zipcodes
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()
    c.execute('SELECT ZipCode FROM WeatherData')
    zipcodes = [row for row in c.fetchall()]
    zipcodes = [i[0] for i in zipcodes]

    if zipcode not in zipcodes:
        #inputs new zipcode into db if not exists
        newZipcode(zipcode)
    else:
        pass

    url = 'http://api.wunderground.com/api/a93323883be13012/hourly/conditions/q/%s.json' % zipcode
    f = urllib.request.urlopen(url)
    json_string = f.read()
    weather = json.loads(json_string)


    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()
    c.execute('UPDATE WeatherData SET Weather = ? WHERE Zipcode = ?', (str(weather), zipcode,))
    conn.commit()
    c.close()

    from WeatherFunctions import *
    SnowFall(weather, zipcode)



zipcode = str(55124)
conn = sqlite3.connect('Alerted.db')
c = conn.cursor()

c.execute('SELECT Weather From WeatherData WHERE Zipcode = ?', (zipcode,))
#converts tuple back to dict
weather = c.fetchone()
p = ''.join(weather)
t = ast.literal_eval(p)

from WeatherFunctions import *
SnowFall(t,zipcode)


