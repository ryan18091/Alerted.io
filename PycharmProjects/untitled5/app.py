import sqlite3
import json

idtag = 123
First_Name = 'Ryan'
Last_Name = 'Erickson'
Address = {'address': '135 Shasta Ct.', 'city': 'Apple Valley', "state":'MN', 'zipcode': '55124'}
email = 'ryanerickson74@gmail.com'
Alerts = [('Weather', '456')]

conn = sqlite3.connect('Alerted.db')
c = conn.cursor()
c.execute('SELECT Email From Users')
users = [row for row in c.fetchall()]
users = [list(elem) for elem in users]
UserEmailList = []
for sublist in users:
    for e in sublist:
        UserEmailList.append(e)

if email not in UserEmailList:
    print('notin')
    address = json.dumps(Address)
    c.execute('INSERT INTO Users (UserID, FirstName, LastName, Address, Email) VALUES (?, ?, ?, ?,?)', (idtag, First_Name, Last_Name,
                                                                                            address, email,))
    conn.commit()
    c.close()



from datetime import datetime
from random import randint
#simulate creation of Alert

#Alert Types
#-Snow Checker prefex 1
alerttype = 1 #User Input, db

def AlertIDCreate(alerttype):
    AlertID = randint(1, 100000000000000)
    AlertID = [int(x) for x in str(AlertID)]
    AlertID.insert(0, alerttype)
    AlertID = ''.join(map(str, AlertID))

    return AlertID

def CreateDatetimeObject(t):

    print(type(t))
    t = datetime.strptime(t, "%H:%M %p")
    return t



AlertID = AlertIDCreate(alerttype)
#checks if AlertID has already been assigned and reasigns if true
conn = sqlite3.connect('Alerted.db')
c = conn.cursor()
c.execute('SELECT AlertID from TimeTrigger')
AlertIDList = [row for row in c.fetchall()]
AlertIDList = [list(elem) for elem in AlertIDList]
if AlertID in AlertIDList:
    AlertID = AlertIDCreate()
else:
    pass

print(AlertID)

trigger = '6:15 am' #User input, db
# trigger = datetime.strptime(trigger, "%H:%M %p")
# print(trigger)

StartWatchTime = '9:00 pm' #User input, db
# StartWatchTime = datetime.strptime(StartWatchTime, "%H:%M %p")
# print(StartWatchTime)

AmountLow = .05 #User Input, db
AmountHigh = 2 #user Input, db

AlertType = 'Time' #Program Generated
Alert = {'Type': AlertType, 'AlertID': AlertID} #Program Generated
AlertedType = 'SMS'
MessageType = 'Standard'
ActionType = {"AlertType": AlertedType, 'Message Type': MessageType}

conn = sqlite3.connect('Alerted.db')
c = conn.cursor()
c.execute('UPDATE Users SET Alerts = ?  Where email=? ', (str(Alert), str(email),))
conn.commit()

c.execute('INSERT INTO TimeTrigger (AlertID, Time, ActionType) VALUES (?,?,?)', (str(AlertID), str(trigger), str(ActionType),))
conn.commit()

c.execute('INSERT INTO SnowFallCheck (AlertID, StarTime, AmountLow, AmountHigh) VALUES (?,?,?,?)', (str(AlertID), str(StartWatchTime),

                                                                                            str(AmountLow), str(AmountHigh),))
conn.commit()
conn.close()


