from sys import exit
from nltk.corpus import words
import inflect


import sqlite3


from flask import Flask
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hangman_dict.db'
# db = SQLAlchemy(app)



conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()


def create_table_order():
    # c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, order VARCHAR)')
    c.execute('CREATE TABLE IF NOT EXISTS orders(game_win INTEGER, game_lose INTEGER, counter INTEGER, choice_order VARCHAR)')


def create_table_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS Word_dict(Word String, Word_length INTEGER)')

def create_table_Plural_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS Plural_Word_dict(Word String, Word_length INTEGER)')


def create_table_New_Word_Dict():
    c.execute('CREATE TABLE IF NOT EXISTS New_Word_dict(Word String, Word_length INTEGER, Date_added DATE, Date_last_used DATE, Usage INTEGER)')

# create_table_order()
# create_table_Word_Dict()
# create_table_New_Word_Dict()
create_table_Plural_Word_Dict()
# c.close()6
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


Most_success = [0,0,0]
counter = (0)



while True:


    game_win = (0)
    game_lose = (0)

    counter += 1
    # word_list = []

    # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
    # word_list = words.words()

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()
    c.execute('From Word_Dict SELECT*')
        for row in row:
            print(row)



    # pluralizes all words in word list
    # print(len(word_list))
    #
    # conn = sqlite3.connect('HangmanSolverdb.db')
    # c = conn.cursor()

    # for word in word_list:
    #     word = word.lower()
    #     c.execute("Insert into Word_dict(Word,Word_length) VALUES (?, ?)", (word, len(word)))
    #
    # conn.commit()
    # c.close()
    # conn.close()
    # exit()

    # engine = inflect.engine()
    # counter = 0
    # plural = []

    # conn = sqlite3.connect('HangmanSolverdb.db')
    # c = conn.cursor()

    # for w in word_list:
    #     # c.execute("Insert into Word_dict(Word,Word_length) VALUES (?, ?)", (w, len(w)))
    #     # conn.commit()
    #     w = w.lower()
    #     p = engine.plural(w)
    #     p = p.lower()
    #     plural.append(p)
    #     counter += 1
    #     print(counter)

    # print(len(plural))
    # print(len(word_list))

    # notin = []
    # print(len(plural))
    # counter = 0
    # for p in plural:
    #     if p not in word_list:
    #         p = p.lower()
    #         counter += 1
    #         print('Counter', counter)
    #         # c.execute("Insert into Plural_Word_dict(Word,Word_length) VALUES (?, ?)", (p, len(p)))
    #         # conn.commit()
    #         notin.append(p)
    #         # print(p)
    #
    # print('not in', len(notin))
    # print('word list',len(word_list))





    # lowercases all words in word_list dictionary
    # word_list = [word.lower() for word in word_list]

    # conn = sqlite3.connect('HangmanSolverdb.db')
    # c = conn.cursor()

    # counter = 0
    # for word in notin:
    #     word = word.lower()
    #     c.execute("Insert into Plural_Word_dict(Word,Word_length) VALUES (?, ?)", (word, len(word)))
    #     conn.commit()
    #     counter += 1
    #     print('Counter2',counter)
    #
    #
    # conn.commit()
    # c.close()
    # conn.close()
    # exit()

    for tweet in tweets_list:


        word = tweet


        alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']

        word_processing_order = []


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

        letter_guessing = False

        while game_over != True:

            # ###### METHOD ######

            tweet = ''.join(word_guess)
            print('Before Guess:   ', tweet)
            from Dict_wort import *
            word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
            from Dict_wort import choice
            print('Character Guess: ',choice)
            i = choice



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


            word = word.lower()
            i = i.lower()
            if i in word:
                alpl.remove(i)


            if i not in word:
                alpl.remove(i)
                turns -= 1

            comp_word = ''.join(word_guess)

            if turns == 0:
                game_lose += 1
                game_over = True
                print("Game LOST:", game_lose)
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                break


            print('After Guess:   ', comp_word)
            print('Turns Remaining:', turns)
            phrase = phrase.lower()
            if comp_word == phrase:
                # print(comp_word)
                game_win += 1
                print('Game Over Win:',game_win)
                game_over = True
                # exit()
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                # order = []
                # exit()
                break

            # print(comp_word)
            # print('Turns Remaining',turns)

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
