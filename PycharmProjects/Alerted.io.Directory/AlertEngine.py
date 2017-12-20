import sqlite3
from datetime import datetime
from WeatherFunctions import WeatherBoolean
import ast


### Iterates over TimeTriggers and ConditionalTriggers for Alers that have evaluated to True and fulfils Alerted Actions
#Engine for TimeTriggers

conn = sqlite3.connect('Alerted.db')
c = conn.cursor()
c.execute('SELECT * From TimeTrigger')
TimeTriggers = [row for row in c.fetchall()]
for line in TimeTriggers:
    time = datetime.strptime(line[1], '%H:%M %p')
    print(line)

    #creates a dict from returned string
    AlertVars = ast.literal_eval(line[3])
    now = (datetime.now())
    td = time - now
    TimeDiff = td.seconds
    zipcode = line[5]
    AlertID = line[0]
    #Checks to see if current time is within 1 minute before to two minutes post trigger time
    # if TimeDiff < 60 or TimeDiff > 86280:
    if TimeDiff:
        #Checks AlertType and calls appropriate function
        AlertID = map(int, str(AlertID))
        if (list(AlertID))[0] == 1:
            AlertCat = 'SnowFall'
            WeatherBoolean(line, time, AlertVars, AlertCat)
    else:
        pass


