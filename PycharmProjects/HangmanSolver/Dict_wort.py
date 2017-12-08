from nltk.corpus import words
from statistics import mode
import sqlite3
import random

import inflect

choice = ()
letter_guessing = False


def guessing_over(tweet, alpl, word_list):

    global choice

    for word in tweet.split():
        if word[0] == '_':
            if '#' in alpl:
                choice = '#'
                return choice
            elif '@' in alpl:
                choice = '@'
                return choice
            else:
                pass

            #### POssible might give this the authority to guess a @ or #


    remaining_letter_list = []
    for word in word_list:
        for l in word:
            if l in alpl:
                remaining_letter_list.append(l)



    # print(remaining_letter_list)

    if remaining_letter_list == []:
        choice = random.choice(alpl)
        # print('1',choice)
        return choice
    else:
        # print(alpl)
        choice = max(set(remaining_letter_list), key=remaining_letter_list.count)
        # print('Remaining in ALPL')
        # print(choice)
        return choice



def word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl):

    global choice


    comparing_words = []

    if len(word_processing_order) == 0:
        guessing_over(tweet, alpl, word_list)
        return choice


    # gets all words from tweeet that equal the currently evaulated word length
    for word in tweet.split():
        # print(word_processing_order)
        if len(word) == word_processing_order[0]:
            comparing_words.append(word)

    possible_words = []


    #creates a list instance of each word in tweet with most common length
    o = []
    for l in comparing_words:
        for i in l:
            o.append(i)

    #checks if those words have been solved, and if so removes [0] from word processing order and sorts new [0] length words from tweet
    if "_" not in o:
        del word_processing_order[0]
            #### Remove all words from wordlist that are of the previous word processing order. Hopefully speeding up itterattion.
        if len(word_processing_order) == 0:
            letter_guessing = True
            guessing_over(tweet, alpl, word_list)
            return choice
        else:
            word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
        return choice


    #Finds all current letters in the most common words and removes all but those letters form list instances of words from
    #the word_list. Then compares the two list instances and if they are equal the str instance of the word is added to the
    #possible_words. (these are the words that the unkown words can still possible be out of the current words in the english dict)

    possible_words_from_dict = []


    for word in word_list:
        if len(word) == word_processing_order[0]:
            possible_words_from_dict.append(word)
        else:
            pass
    # print(len(comparing_words))
    # print(len(possible_words_from_dict))
    # print(possible_words_from_dict)
    for l in comparing_words:
        print(l)
        let_list = []
        for char in l:
            let_list.append(char)
        for i in possible_words_from_dict:
            u = list(i)
            for n, t in enumerate(u):
                if t not in let_list:
                    u[n] = '_'
            if u == let_list:
                possible_words.append(i)
    # print(possible_words)

    # checks to see if no possibel words where found. If so, the function is started over after the removeal of [0] from word processing order
    if len(possible_words) == 0:
        del word_processing_order[0]
        if len(word_processing_order) == 0 and len(possible_words) == 0:
            letter_guessing = True
            guessing_over(tweet, alpl, word_list)
            return choice
        else:
            word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
        return choice




    #creates a list of all the letters in the possibel word list and sorts them according to most common to least
    letter_list = []
    for word in possible_words:
        for char in word:
            letter_list.append(char)

    from collections import Counter
    c = Counter(letter_list)
    first_letter_choice_tup = c.most_common(36)
    choice_list = []
    for j, k in first_letter_choice_tup:
        if j in alpl:
            choice_list.append(j)

    # print('Most common letters available in possible words in descending order',choice_list)


    if len(choice_list) == 0:
        del word_processing_order[0]
        # print('No possible words for this length with letters remaining available --- Deleting word order[0] --- starting func. over')
        if len(word_processing_order) == 0 and len(choice_list) == 0:
            letter_guessing = True
            guessing_over(tweet, alpl, word_list)
            return choice
        else:
            word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl)
        return choice



    if len(choice_list) > 0:
        choice = choice_list[0]
        return choice














