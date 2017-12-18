import sqlite3
from time import sleep

conn = sqlite3.connect('Alerted.db')
c = conn.cursor()

global weather
weather = ()


class WeatherQuery(object):

    def __init__(self, zipcode,query_term):
        self.zipcode = zipcode
        self.query_term = query_term

    def ZipcodeSearch(self):
        c.execute('SELECT * FROM WeatherData WHERE Zipcode=?', (self.zipcode,))
        weather = {row for row in c.fetchall()}
        return weather


weatherLookup = WeatherQuery('55124', None)
weather2 = weatherLookup.ZipcodeSearch()

if weather2 != weather:
    # print(weather2)
    weather = weather2





# c.execute('ALTER TABLE WeatherData ADD COLUMN SnowFall3hr INTEGER')
# conn.commit()