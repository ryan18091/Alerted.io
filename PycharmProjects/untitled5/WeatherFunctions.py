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
            snowfall['SnowFall']['SnowFallTotal'] = [0.01]
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
            snowfallList.append(float(0.1))
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
    snowfall = ast.literal_eval(snowfall)
    obstime = weather['current_observation']['observation_time_rfc822']
    # obstime = datetime_converstion(obstime)


    SnowFallWeekly(snowfall, weather, zipcode, obstime)

#Inputs a new zipcode into the zipcode list
def newZipcode(zipcode):
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()

    snowfall = {'SnowFall': {'obstime': None, 'SnowFallTotal': None}}

    c.execute('INSERT INTO  WeatherData (Zipcode, SnowFall) VALUES (?,?)', (zipcode, str(snowfall),))
    conn.commit()

def SnowFallAmount(hours, zipcode, AmountLow, AmountHigh, AlertVars, AlertCat, AlertTime, SnowFallStartTime):
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()
    c.execute('SELECT SnowFall From WeatherData Where Zipcode=?', (zipcode,))
    SnowFallDict = c.fetchone()
    SnowFallDict = SnowFallDict[0]
    SnowFallDict = ast.literal_eval(SnowFallDict)
    snowfall = (SnowFallDict['SnowFall']['SnowFallTotal'])
    snowfall = snowfall[-hours:]
    TotalSnowFall = sum(snowfall)
    #Checks to see if TotalSnow Fall falls between Low and High Amount and triggers Alert Type:
    if TotalSnowFall < AmountHigh and TotalSnowFall > AmountLow:
        SMSVars = [AlertVars, AlertCat, AlertTime, SnowFallStartTime, TotalSnowFall, zipcode]
        if AlertVars['AlertType'] == 'SMS':
            from TwillioSMS import SMS
            SMS(SMSVars)
            pass
        elif AlertVars['AlertType'] == 'Email':
            pass





#Returns true of false if snow fall amount over specific time equals given value
def WeatherBoolean(line,time, AlertVars, AlertCat):
    print(line)
    conn = sqlite3.connect('Alerted.db')
    c = conn.cursor()
    zipcode = line[5]
    AlertTime = line[1]
    AlertID = line[0]

    #Creates n hours before alert time that Snow Fall should be checked
    c.execute('SELECT * FROM SnowFallCheck WHERE AlertID =? ', (AlertID,))
    SnowFallReqs = [row for row in c.fetchone()]
    print(SnowFallReqs)
    AmountLow = SnowFallReqs[2]
    AmoutnHigh = SnowFallReqs[3]
    conn.close()
    SnowFallStartTime = datetime.strptime(SnowFallReqs[1], '%H:%M')
    print(SnowFallStartTime)
    td = time - SnowFallStartTime
    t = ((td.seconds/60)/60)
    hours = (round(t))

    SnowFallAmount(hours, zipcode, AmountLow, AmoutnHigh, AlertVars, AlertCat, AlertTime, SnowFallStartTime)



# class WeatherQuery(object):
#
#     def __init__(self, ):