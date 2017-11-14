from nltk.corpus import words
import itertools
import operator



# most_occuring_length = []
# word_processing_order = []
# word_list = []
# choice = ()
# letter_list = []
#
#
#
#
#
# # choice_list = []
#
# alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']








#The purpose of this program is to solve the Political Hangman game at politicalhangman.com
#The program is only given the dynamic information shown to a user as they are playing the game. This algorythim attempts
#to solve the game by solving the unkown words. It attempts to solve the words that have a length most commonly found in
#in the english dictionary. Giving the highest chance that a letter choice will be found in that word. It then sorts the
#remaining words of a that specific length and gueeses again the most common letter found in the remaining words. Repeating
#this process allows the algorithem to sort possible words and continue it's most probable character guessing. Once a
#word has been solved the next most common length of word is attempted to be solves using the same patter, but now using
#the additional information of letters in that have been correctly guessed and characters remaining that can be guessed.

#
#
# # tweet = "I was proud to endorse BilldeBlasio tonight He is leading the city in a way that brings people together to make a better life for all"
# tweet = '_____ _____ __ ______________ _____ _______ _ _____ ____ _________ __ __ ____ ________ _ __ _____ _________ ___________ _____'
# tweet = '_ __ ___ ____ ______'


# def highest_prob_length_let(alpl, tweet):
choice = ()
word_processing_order = []


def word_proc_order(tweet, word_processing_order):
    global word_list
    # global word_processing_order

    word_length_order = []
    word_length_list = []
    most_occuring_length = []
    # word_processing_order = []



    # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
    word_list = words.words()
    # lowercases all words in word_list dictionary
    word_list = [word.lower() for word in word_list]
    length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    length_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
                   16: 0, 17: 0, 18: 0, 19: 0, 20: 0}

    for word in word_list:
        for num in length:
            if len(word) == num:
                length_dict[num] = length_dict[num] + 1

            else:
                pass

    for w in sorted(length_dict, key=length_dict.get, reverse=True):
        a = w, length_dict[w]
        most_occuring_length.append(a)
        word_length_order.append(w)

    print('Most occuring lengths of words in English Dict', most_occuring_length)

    # print(word_length_order) #--- Most common lengths of words in dict order

    # Writes to list the length of each word in tweet
    word_lengths = (list(map(len, tweet.split())))
    # print(word_lengths)  #--- lengths of words in tweet



    # determines what length of word in tweet exists in word_length_order and returns the first same length as x
    for length in word_length_order:
        if length in word_lengths:
            if length not in word_processing_order:
                word_processing_order.append(length)
                # print('pass')

    print('Most occuring lengths of words in tweet', word_processing_order)


                # return word_processing_order


# def highest_prob_length_let(tweet, alpl):


def first_choice(tweet,alpl):

    from ML_test1 import choice
    global choice


    # global choice
    # global alpl
    global word_processing_order
    global word_list


    #added for testing
    # global tweet

    most_occuring_length = []
    word_length_order = []
    word_length_list = []
    # word_processing_order = []
    # word_lengths = []
    # x = ()
    # choice = ()
    letter_list = []

    word_proc_order(tweet, word_processing_order)

    x = word_processing_order[0]
    print('Word Length to be processed', x)


    # print(word_lengths)  #--- lengths of words in tweet
    # print(word_processing_order) #--- Processing Order for lengths of words in tweet

    # creates a list of words from the dictionary/word_list that have the same
    #  length as the most common length  of word from the tweet
    for word in word_list:
        if len(word) == x:
            word_length_list.append(word)
        else:
            pass

    for word in word_length_list:
        for char in word:
            letter_list.append(char)

    # print(choice)
    # The counter determines which letter is most common
    # in all of the possible words with the most common length
    from collections import Counter
    c = Counter(letter_list)
    first_letter_choice_tup = c.most_common(36)
    choice_list = []
    for j, k in first_letter_choice_tup:
        if j in alpl:
            choice_list.append(j)
    choice = choice_list[0]
    print('Most common letters in most common word length being processes', choice_list)
    print('Most common letter still in alpl choices', choice)
    # alpl.remove(choice)
    # print(word_processing_order)
    # print(word_length_order)


    ###added for testing
    # tweet = 'hypotaxia acrospire bip___ic'
    print('final',choice)

    return choice

def word_guessing(tweet,alpl):

    global word_processing_order
    global choice
    global wo

    if len(word_processing_order) == 0:

        word_proc_order(word_processing_order)

    # while True:
    print('top')
    comparing_words = []


    #gets all words from tweeet that equal the currently evaulated word length
    for word in tweet.split():
        if len(word) == word_processing_order[0]:
            comparing_words.append(word)

    possible_words = []

    o = []
    for l in comparing_words:
        for i in l:
            o.append(i)

    if "_" not in o:
        comparing_words = []
        del word_processing_order[0]
        for word in tweet.split():
            if len(word) == word_processing_order[0]:
                comparing_words.append(word)


    print('Word Length to be processed', word_processing_order[0])
    print('comparing words',comparing_words)
    print("word list length", len(word_list))



    for l in comparing_words:
        print(l)
        let_list = []
        for char in l:
            let_list.append(char)
        for i in word_list:
            # print(i)
            u = list(i)
            # print(u)
            for n,t in enumerate(u):
                if t not in let_list:
                    u[n] = '_'
            # print(u)
            if u == let_list:
                # print(i)
                possible_words.append(i)
            # if u == let_list:
            #     new_idea.append(word)

    print(possible_words)

    if  len(possible_words) == 0:
        print('HHHHHHHHH')
        del word_processing_order[0]
        word_guessing(tweet, alpl)
        return choice


    letter_list = []
    for word in possible_words:
        for char in word:
            letter_list.append(char)
    print('letter list', letter_list)


    #### Break possible words apart and return most common letter as the guess
    from collections import Counter
    c = Counter(letter_list)
    first_letter_choice_tup = c.most_common(36)
    choice_list = []
    for j, k in first_letter_choice_tup:
        if j in alpl:
            choice_list.append(j)
    # print(first_letter_choice_tup)
    # print(choice_list)

    print('choice list', choice_list)
    print(choice_list[0])
    choice = choice_list[0]
    print('Most common letters in most common word length being processes', choice_list)
    print('Most common letter still in alpl choices', choice)

    # print(first_letter_choice_tup)
    # print(choice)
    return choice

def highest_prob_length_let(tweet, alpl):

    #Innitiates the word_guess function after the initial letter guess is made successfully.
    # while True:
    for word in tweet.split():
        for char in word:
            if char != "_":
                word_guessing(tweet, alpl)
                return choice

    first_choice(tweet,alpl)

    # print('here',choice)
    return choice

# highest_prob_length_let(tweet, alpl)
# print(choice)



