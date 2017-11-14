import sqlite3
import time
from datetime import datetime

import tweepy
import json


# Opening connection to DB
conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()

def create_table_Tweets():
    c.execute('CREATE TABLE IF NOT EXISTS Tweets(politician VARCHAR, tweet TEXT, Json_blob TEXT)')

def create_table_Gamedb():
    c.execute('CREATE TABLE IF NOT EXISTS game_db(session_id INTEGER, politician VARCHAR, politician_id INTEGER,'
              'datestamp TEXT, turns INTEGER, guess_phrase TEXT, remaining_letters TEXT, word_guess TEXT, phrase TEXT, alpl TEXT)')



create_table_Tweets()
c.close()
conn.close()

consumer_key = "aUFAZkqkewIzVEXODSeN04Y1v"
consumer_secret = "XH0s8fpvae4fMfP9llv835kY3rMcXAdcokyUi42bvF4PL8GUsm"
access_token = "2401698925-wTLiLofze7MlQ4mlE5bp8l8XhIzIR8ZQmucqfVk"
access_token_secret = "42AoblxektQ2NmKmayacgEmaDbxRZYzUvLIdVgUCbvFXi"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
global number

number = 0
# for politician in pol_list:
from Senators_IDs import t_dict

for politician, politician_id in t_dict.items():

    print(politician)
    print("Twitter API Engine Running...")

    for tweet in tweepy.Cursor(api.user_timeline, id=politician_id, tweet_mode='extended').items(1000):




        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):


            try:

                t = (tweet)
                i = (tweet.full_text)
                tweetdump = (tweet._json)
                json_tweet = json.dumps(tweetdump)

                mystring = str(t)



                if 'http' in i:
                    i = i[:-24]

                if 'https' in i:
                    num = i.find('https')
                    l = len(i)
                    p = num - l
                    i = i[:p]

                if '&amp' in i:
                    i = i.replace("&amp", "&")

                s = i
                s = s.replace(" ", "")
                if len(s) == 0:
                    continue


                def tweet_entry():

                    global number

                    number = number + 1


                    conn = sqlite3.connect('HangmanSolverdb.db')
                    c = conn.cursor()

                    c.execute("INSERT INTO Tweets (politician, tweet, Json_blob) VALUES (?, ?, ?)", (politician, i, json_tweet))
                    print(i)
                    conn.commit()
                    # c.close()
                    conn.close()


                tweet_entry()



            except tweepy.TweepError as e:
                print('Tweepy Error')
                print(e.reason)
                sleep(10)
                continue
            except StopIteration:
                break


        if (tweet.retweeted) and ('RT @' in tweet.text):
            print('Retweet')
            continue

        if number == 100:
            number = 0
            break




