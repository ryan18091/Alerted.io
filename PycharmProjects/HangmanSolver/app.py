from sys import exit
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

import textwrap

from Methods import*
app = Flask(__name__)


# SQLALCHEMY_DATABASE_URI = 'sqlite:///HangmanSolver.db'
# db = SQLAlchemy(app)

conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()

def create_table_order():
    # c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, order VARCHAR)')
    c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, choice_order VARCHAR)')

create_table_order()
# c.close()
# conn.close()

tweets_list = []
number = (0)

def read_from_db():
    global tweets_list
    global number
    c.execute("SELECT * FROM Tweets")
    for row in c.fetchall():
        tweets = (row[1])
        tweets_list.append(tweets)


read_from_db()
c.close()
conn.close()

# game_win = (0)
# game_lose = (0)
Most_success = [0,0,0]
counter = (0)
gam


while True:

    game_win = (0)
    game_lose = (0)

    counter += 1

    for tweet in tweets_list:


        word = tweet


        alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']

        word_guess = []
        turns = ()
        phrase = []
        guessed_not_in = []
        guessed_in = []
        game_over = ()



        for char in word:
            for l in alpl:
                if char == l:
                    word_guess.append('_')
                    phrase.append(l)

                    break

                if char == l.upper():
                    word_guess.append('_')
                    phrase.append(l.upper())
                    break

                if char == ' ':
                    word_guess.append(' ')
                    phrase.append(' ')
                    break



        phrase = ''.join(phrase)
        print(phrase)
        print(word_guess)

        l = len(phrase)

        l = int(l / 10)

        if l >= 10:
            turns = 4
        if l <= 9 and l >= 7:
            turns = 5
        if l <= 6 and l >= 5:
            turns = 6
        if l <= 4 and l >= 3:
            turns = 7
        if l <= 2:
            turns = 8


        choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']

        order =[]

        while len(choices) != 0:
            x = random.choice(choices)
            order.append(x)
            choices.remove(x)



        while game_over != True:


            # ###### METHOD ######

            for i in order:


                if i == '@' or '#':
                    for letter in range(len(phrase)):
                        if i == phrase[letter]:
                            word_guess[letter] = i

                if str.isnumeric(i):
                    for letter in range(len(phrase)):
                        if i == phrase[letter]:
                            word_guess[letter] = i
                        elif ' ' == phrase[letter]:
                            word_guess[letter] = ' '

                if str.islower(i):
                    for letter in range(len(phrase)):
                        if i == phrase[letter]:
                            word_guess[letter] = i
                        elif ' ' == phrase[letter]:
                            word_guess[letter] = ' '

                i = i.upper()

                if str.isupper(i):
                    for letter in range(len(phrase)):
                        if i == phrase[letter]:
                            word_guess[letter] = i
                        elif ' ' == phrase[letter]:
                            word_guess[letter] = ' '

                if i in word:
                    guessed_in.append(i)

                if i not in word:
                    guessed_not_in.append(i)
                    turns -= 1

                if turns == 0:
                    game_lose += 1
                    a = len(guessed_in)
                    b = len(guessed_not_in)
                    c = float(a) / float(b)
                    game_over = True
                    alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']


                comp_word = ''.join(word_guess)

                if comp_word == word:
                    # print(comp_word)
                    game_win += 1
                    # print('Game Over Win')
                    game_over = True
                    alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                    # order = []
                    # exit()
                    break


    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()

    ###### get all data from wins colomn, create variable for greatest amount of wins for if loop below#####
    c.execute("SELECT game_win FROM orders")
    rows = c.fetchall()
    for row in rows:
        max_wins = max(row)


    conn.commit()
    # conn.close()
    c.close()

    # print(game_win)
    # print(game_lose)
    # print(max_wins)
    if game_win >= max_wins:

        Most_success = []

        Most_success.insert(0, game_win)
        Most_success.insert(1, game_lose)
        Most_success.insert(2, order)

        conn = sqlite3.connect('HangmanSolverdb.db')
        c = conn.cursor()

        order = ''.join(order)


        print(type(game_win))
        print(type(game_lose))
        print(type(counter))
        print(type(order))



        c.execute("INSERT INTO orders (game_win, game_lose, counter, choice_order) VALUES (?, ?, ?, ?)", (game_win, game_lose, counter, order))
        conn.commit()
        conn.close()

        # print('new high score',Most_success)
        game_win = (0)
        game_lose = (0)
