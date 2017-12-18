import sqlite3
import ast
from datetime import datetime

#Creates a Datatime object
def datetime_converstion(lastobstime):

    lastobstime = lastobstime.split()
    monthConversion = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                       'Oct': 10, 'Nov': 11, 'Dec': '12'}
    for n, i in enumerate(lastobstime):
        if i in monthConversion:
            lastobstime[n] = monthConversion[i]

    lastobstime = lastobstime[1:]
    lastobstime = lastobstime[:-1]
    lastobstime = ' '.join(lastobstime)
    lastobstime = datetime.strptime(lastobstime, '%d %m %Y %H:%M:%S')
    return lastobstime

#inputs snow fall data as a list according to zipcodes
def SnowFallWeekly(snowfall, weather, zipcode, obstime):

    temp = (weather['current_observation']['temp_f'])
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()

    lastobstime = snowfall['SnowFall']['obstime']
    if lastobstime == None:
        snowfall['SnowFall']['obstime'] = obstime
        if int(temp) <= 32.0:
            snowfall['SnowFall']['SnowFallTotal'] = [((float(weather['current_observation']['precip_1hr_in'])) * 16)]
            c.execute('UPDATE WeatherData Set SnowFall = ? WHERE Zipcode = ?', (str(snowfall), zipcode,))
            conn.commit()
            return
        else:
            snowfall['SnowFall']['SnowFallTotal'] = [0.00]
        c.execute('UPDATE WeatherData Set SnowFall = ? WHERE Zipcode = ?', (str(snowfall), zipcode,))
        conn.commit()
        return
    else:
        pass


    # snowfall = snowfall['TwoHourSnow']['SnowFallTotal']
    snowfallList = snowfall['SnowFall']['SnowFallTotal']
    print(len(snowfallList))
    if len(snowfallList) < 168:
        if int(temp) <= 32.0:
            print('1 under 32')
            snowfall.index(0, (float(weather['current_observation']['precip_1hr_in']) * 16))
            snowfall['SnowFall']['SnowFallTotal'] = snowfall
            snowfall['SnowFall']['obstime'] = obstime
        else:
            print('2over 32')
            snowfallList.append(float(0.0))
            print(snowfallList)
            snowfall['SnowFall']['SnowFallTotal'] = snowfallList
            snowfall['SnowFall']['obstime'] = obstime
    elif len(snowfallList) == 168:
        snowfallList.pop(0)
        if int(temp) <= 32.0:
            print('under 32')
            snowfallList.append(float((float(weather['current_observation']['precip_1hr_in']) * 16)))
            snowfall['SnowFall']['SnowFallTotal'] = snowfallList
            snowfall['SnowFall']['obstime'] = obstime
        else:
            print('over 32')
            snowfallList.append(float(0.0))
            print(snowfallList)
            snowfall['SnowFall']['SnowFallTotal'] = snowfallList
            snowfall['SnowFall']['obstime'] = obstime

    c.execute('UPDATE WeatherData Set SnowFall = ? WHERE Zipcode = ?', (str(snowfall), zipcode,))
    conn.commit()


#updates Snowfall Dictionary across all Hour metrics
def SnowFall(weather,zipcode):


    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()
    c.execute('SELECT SnowFall FROM WeatherData WHERE Zipcode = ?', (zipcode,))
    snowfall = c.fetchone()
    snowfall = snowfall[0]
    print(snowfall)
    print(type(snowfall))
    # snowfall = ''.join(snowfall)
    snowfall = ast.literal_eval(snowfall)
    obstime = weather['current_observation']['observation_time_rfc822']
    # obstime = datetime_converstion(obstime)


    SnowFallWeekly(snowfall, weather, zipcode, obstime)

def newZipcode(zipcode):
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()

    snowfall = {'SnowFall': {'obstime': None, 'SnowFallTotal': None}}

    c.execute('INSERT INTO  WeatherData (Zipcode, SnowFall) VALUES (?,?)', (zipcode, str(snowfall),))
    conn.commit()


# class WeatherQuery(object):
#
#     def __init__(self, ):