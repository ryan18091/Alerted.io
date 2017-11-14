from nltk.corpus import words
from statistics import mode
import inflect

choice = ()
letter_guessing = False


def guessing_over(tweet, alpl, word_list):

    global choice

    for word in tweet.split():
        if word[0] == '_':
            print(word)
            print(tweet)
            exit()

    if 's' in alpl:
        choice = 's'
        return choice
    # elif '#' in alpl:
    #     choice = '#'
    #     return choice
    # elif '@' in alpl:
    #     choice = '@'
    #     return choice
    # else:
    #     pass


    # if len(word_list) == 0:
    #     # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
    #     word_list = words.words()
    #     # pluralizes all words in word list
    #     engine = inflect.engine()
    #     for w in word_list:
    #         p = engine.plural(w)
    #         if p not in word_list:
    #             word_list.append(p)
    #     # lowercases all words in word_list dictionary
    #     word_list = [word.lower() for word in word_list]



    remaining_letter_list = []
    for word in word_list:
        for l in word:
            if l in alpl:
                remaining_letter_list.append(l)


    choice = mode(remaining_letter_list)
    return choice






def word_sort(letter_guessing, word_list, word_processing_order, tweet, alpl):

    global choice

    word_length_order = []
    most_occuring_length = []
    comparing_words = []


    if letter_guessing == True:
        guessing_over(alpl, word_list)
        return choice


    # if len(word_list) == 0:
    #     # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
    #     word_list = words.words()
    #     # lowercases all words in word_list dictionary
    #     word_list = [word.lower() for word in word_list]

    if len(word_processing_order) == 0:
        # # Takes all words in english dictionary and orders the lengths of the words from most common to least - word_length_order
        # word_list = words.words()
        # #pluralizes all words in word list
        # engine = inflect.engine()
        # for w in word_list:
        #     p = engine.plural(w)
        #     print(p)
        #     # if p not in word_list:
        #     #     word_list.append(p)
        #
        # # lowercases all words in word_list dictionary
        # word_list = [word.lower() for word in word_list]


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


        # Writes to list the length of each word in tweet
        word_lengths = (list(map(len, tweet.split())))

        # creates the word
        for length in word_length_order:
            if length in word_lengths:
                if length not in word_processing_order:
                    word_processing_order.append(length)

    # gets all words from tweeet that equal the currently evaulated word length
    for word in tweet.split():
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
        comparing_words = []
        del word_processing_order[0]
        # print('1 - Current word length is fully solved --- Deleting word order[0] --- starting func. over')
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
    for l in comparing_words:
        let_list = []
        for char in l:
            let_list.append(char)
        for i in word_list:
            u = list(i)
            for n, t in enumerate(u):
                if t not in let_list:
                    u[n] = '_'
            if u == let_list:
                possible_words.append(i)

    # print('Word Processing Order', word_processing_order)
    # print('Length being evaluated', word_processing_order[0])
    # print('Words from tweet matching evaluating length', comparing_words)
    # print("Possible Words that still match words from tweet", possible_words)


    # checks to see if no possibel words where found. If so, the function is started over after the removeal of [0] from word processing order
    if len(possible_words) == 0:
        # print('No possible words for this length --- Deleting word order[0] --- starting func. over')
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














