import sqlite3


conn = sqlite3.connect('Alerted.db')
c = conn.cursor()

# c.execute('INSERT INTO  WeatherData (Zipcode, SnowFall) VALUES (?,?)', (zipcode, str(snowfall),))

c.execute('DELETE  FROM Users')

# c.execute('ALTER TABLE Users ADD COLUMN Email STRING')
conn.commit()
c.close()
