from sys import exit
from nltk.corpus import words
import inflect
from datetime import datetime

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
    c.execute('CREATE TABLE IF NOT EXISTS New_Word_dict1(Word String, Word_length INTEGER, Date_added NUMERIC, Date_last_used DATE, Usage INTEGER)')


def create_table_Tests():
    c.execute('CREATE TABLE IF NOT EXISTS Tests1(Games_Won Integer, Games_Lost INTEGER,  Description STRING)')

def create_table_Games_lost():
    c.execute('CREATE TABLE IF NOT EXISTS Games_Lost1(Tweet_Original String, Tweet_Guessed String, Letters_Remaining String, Test_Description String)')


def create_table_Emphasis_List():
    c.execute('CREATE TABLE IF NOT EXISTS Emphasis_List1(word String)')



create_table_order()
create_table_Word_Dict()
create_table_New_Word_Dict()
create_table_Games_lost()
create_table_Plural_Word_Dict()
create_table_Emphasis_List()
create_table_Tests()
# c.close()
# conn.close()

tweets_list = []
number = (0)

description = 'Started to Use learning ALG with emphasis Dict'



def learn_from_tweet():
    new_words = []
    for word in tweet_learning.split():
        if word.lower() not in word_list:
            new_words.append(word)
    print(new_words)

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()
    new_words_db = []
    c.execute('SELECT * FROM New_Word_Dict1')
    for row in c.fetchall():
        n_word = (row[0])
        new_words_db.append(n_word)

    for word in new_words:
        if word not in new_words_db:
            time = (datetime.now())
            word = word.lower()
            c.execute('INSERT INTO New_Word_Dict1(Word, Word_length, Date_added) VALUES(?,?,?)',(word,len(word), time))
            conn.commit()
            word_list.append(word.lower())

    c.close()
    conn.close()

def read_from_db():
    global tweets_list
    global number
    c.execute("SELECT * FROM Tweets")
    counter = 0
    for row in c.fetchall():
        if counter == 300:
            break
        else:
            counter += 1
            tweets = (row[1])
            tweets_list.append(tweets)



read_from_db()
c.close()
conn.close()


Most_success = [0,0,0]
counter = (0)
game_engine = True
game_cycles = 0


while game_engine == True:


    game_win = (0)
    game_lose = (0)

    counter += 1
    # word_list = []

    # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
    # word_list = words.words()

    word_list = []
    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()
    c.execute('SELECT* from Word_Dict')
    for row in c.fetchall():
        word = str(row[0])
        word_list.append(word)

    c.execute('SELECT  * from Plural_Word_Dict')
    for row in c.fetchall():
        word = str(row[0])
        word_list.append(word.lower())

    c.execute('SELECT *from New_Word_dict1')
    for row in c.fetchall():
        if row[0] not in word_list:
            word = str(row[0])
            word_list.append(word.lower())

    word_list = list(set(word_list))

    c.execute('SELECT * FROM Emphasis_List1')
    for row in c.fetchall():
        word = str(row[0])
        word_list.append(word.lower())


    word_length_order = []
    most_occuring_length = []

    #Gets the order of most common word lengths in the current word_list/Dictionary
    length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    length_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
                   16: 0, 17: 0, 18: 0, 19: 0, 20: 0}

    # print('here',len(word_list))
    for word in word_list:
        word = str(word)
        for num in length:
            if len(word) == num:
                length_dict[num] = length_dict[num] + 1

            else:
                pass

    for w in sorted(length_dict, key=length_dict.get, reverse=True):
        a = w, length_dict[w]
        most_occuring_length.append(a)
        word_length_order.append(w)


    for tweet in tweets_list:


        alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']


        word_guess = []
        turns = ()
        phrase = []
        guessed_not_in = []
        guessed_in = []
        game_over = ()



        for char in tweet:
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

        tweet_learning = phrase



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

        word_lengths = (list(map(len, tweet.split())))
        # print(type(tweet))
        # print(tweet)
        t = tweet.split()
        # print(t)
        # print(word_lengths)
        word_processing_order = []

        # creates the word length processing order for the given tweet based upon the most common word lengths in the word_list
        for length in word_length_order:
            for word in t:
                if length == len(word):
                    word_processing_order.append(length)
                    break

        turn_counter = 0
        turns_amount = turns
        # print(word_processing_order)

        while game_over != True:

            # ###### METHOD ######

            tweet = ''.join(word_guess)
            print('Before Guess:   ', tweet)
            from Dict_wort import *
            word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
            from Dict_wort import choice




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


            phrase = phrase.lower()
            i = i.lower()
            if i in phrase:
                alpl.remove(i)

            if i not in phrase:
                alpl.remove(i)
                turns -= 1
                turn_counter += 1

            comp_word = ''.join(word_guess)

            print('Character Guess: ', choice)
            print('Hangman Phrase: ', phrase)

            if turns == 0:
                learn_from_tweet()
                learn_from_tweet()
                game_lose += 1
                game_over = True
                conn = sqlite3.connect('HangmanSolverdb.db')
                c = conn.cursor()
                # print(type(phrase))
                # print(type(comp_word))
                # print(type(alpl))
                # print(type(description))

                alpl = ''.join(alpl)

                # c.execute("INSERT INTO Games_Lost1(Tweet_Original,Tweet_Guessed, Letters_Remaining, Test_Description) VALUES (?,?,?,?)",
                #           (phrase, comp_word, alpl, description))
                # conn.commit()
                comp_word = comp_word.split()
                phrase = phrase.split()
                # print(comp_word)
                let_list = []
                for word in comp_word:
                    for char in word:
                        let_list.append(char)

                # print(let_list)

                #Create Learning DB creation
                conn = sqlite3.connect('HangmanSolverdb.db')
                c = conn.cursor()
                for i in phrase:
                    print(i)
                    u = list(i)
                    for n, t in enumerate(u):
                        if t not in let_list:
                            u[n] = '_'
                        print(u)
                        if "_" in u:
                            print('_ in u')
                            print(i.lower())
                            if i.lower() in word_list:
                                print(i)
                                print(type(i))
                                c.execute('INSERT INTO Emphasis_list1(word) VALUES (?)',(i,))
                                conn.commit()
                                break
                c.close()
                conn.close()
                print('Game Over Win:', game_win)
                print('Games Lost:', game_lose)
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                learn_from_tweet()
                break


            print('Turns Remaining:', turns)
            phrase = phrase.lower()
            comp_word = comp_word.lower()
            if comp_word == phrase:
                # print(comp_word)
                game_win += 1
                print('Game Over Win:',game_win)
                print('Games Lost:',game_lose)
                game_over = True
                alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
                learn_from_tweet()
                break

            # print(comp_word)
            # print('Turns Remaining',turns)

    conn = sqlite3.connect('HangmanSolverdb.db')
    c = conn.cursor()

    ###### get all data from wins colomn, create variable for greatest amount of wins for if loop below#####
    # c.execute("SELECT game_win FROM orders")
    # rows = c.fetchall()
    # for row in rows:
    #     max_wins = max(row)

    c.execute("INSERT INTO Tests1(Games_Won, Games_Lost, Description) VALUES (?,?,?)",(game_win, game_lose,description))
    conn.commit()
    c.close()
    conn.close()
    # game_engine = False
    game_cycles += 1











    # print(length_dict)
    # print(most_occuring_length)
    # print(word_length_order)


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



