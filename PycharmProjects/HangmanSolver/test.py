import sqlite3


conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()

###### get all data from wins colomn, create variable for greatest amount of wins for if loop below#####
c.execute("SELECT game_win FROM orders")
rows = c.fetchall()
for row in rows:
    max_wins = max(row)


conn.commit()
c.close()