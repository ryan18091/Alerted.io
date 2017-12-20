import sqlite3


conn = sqlite3.connect('Alerted.db')
c = conn.cursor()

# c.execute('INSERT INTO  WeatherData (Zipcode, SnowFall) VALUES (?,?)', (zipcode, str(snowfall),))


# c.execute('DROP TABLE Users')
# c.execute('DELETE FROM Users')

# c.execute('ALTER TABLE TimeTrigger ADD COLUMN Zipcode Integer')

c.execute('UPDATE SnowFallCheck SET StarTime = ? WHERE AlertID = ?', ( '21:00', str(131404245573760)))


def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS Users(UserID INTEGER, FirstName TEXT, LastName TEXT, Address Text, Email Text, Alerts Text)')
    conn.commit()
createTable()
#
def createTable1():
    c.execute('CREATE TABLE IF NOT EXISTS SnowFallCheck(AlertID INTEGER, StarTime TEXT, AmountLow INTEGER, AmountHigh INTEGER)')
    conn.commit()
createTable1()




conn.commit()
c.close()
