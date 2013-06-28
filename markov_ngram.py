#!/usr/bin/env python
#Hackbright exercise 8
# 6.27.13

import sys
import random
import re


def make_chains(corpus, ngram): #ngram is the size of the key tuple
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #########start with a string = corpus and a # for the ngram###############
    text = corpus.split() # turns the string into a list

    #######create our initial tuple. this is the # of words in each key######
    tuple_size = ngram
    first_key = []
    for i in range(tuple_size):         #range is 0, 1, ..., to the size the tuple
        word = text.pop(0)               #pops the first item off text, shortens list
        first_key.append(word)          #appends this to our first_key until we have an n-gram

    key = tuple(first_key)              # changes the resulting list to a tuple

    ####################create dictionary of key,value##########################
    chains = {}  #this is our empty chains dictionary

    while text:  
        val = text.pop(0)               #loop executes until text list is empty
        if chains.get(key):            # if the key pair already exists
            chains[key].append(val)    # append to the value list
        else:
            chains[key] = [val]        # creates value list for that new key

        key = key[1:] + (val,)         # the new key stars with the 2nd word
                                       # (val) is a string, but (val,) is a tuple
    return chains
    #################################################################################
#----------------------------------first recusive(not as effecient)--------------------
# def first_key(chains):
#     current_key = random.choice(chains.keys())  #key is a tuple
#     #print current_key
   
#     rstring = str(current_key[0]) 
#     #print "[first_key] comparing %r to %r" % (rstring, rstring.capitalize())                 #rstring is a string
    
#     if rstring == rstring.capitalize():         #capitalize is a string function
#         return current_key                      #return a tuple
#     else:
#         return first_key(chains) 
#-------------------------------------------------------------------------------------

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""                          

    text_list = []                        # this is a list

    ##############this chooses a random key. Only once in the program#########  
    
    current_key = random.choice(chains.keys())  #key is a tuple
    rstring = str(current_key[0])               #checks the first word in the tuple. 
                                                # capitalize function works on a string

    #########Check tuple and start text list w/ capitalize word################
    while rstring != rstring.capitalize():
       
        current_key = random.choice(chains.keys())  # picks another key
        #print "current_key:", current_key
        rstring = str(current_key[0])               # reassign the new first word in the tuple
                                                    #   to check

    text_list = list(current_key)
    
    ############################### loop thru values for more text#################

    while chains.get(current_key, None):        #tests that there is a value for the key
       
        value_list = chains[current_key]                # list of all value for each key
        
        random_word = random.choice(value_list)        # picks a random word in value_list
        
        text_list.append(random_word)          # adding random value to list
        text_list_len = len(" ".join(text_list)) # makes it a string and counts chars

        if text_list_len >= 100: 
                                               # after 100 char, check for punct
            if re.match("(?!.)", random_word):
                break

        current_key = current_key[1:] + (random_word,) # reassign current key with new pair
        

    return " ".join(text_list)
    ####################################################################################

def main():
    args = sys.argv                      #args is the list (markov.py, inputfile, ngram)

    src_one =open(args[1]).read()        #args[1] is the name of the src_one.
    src_two =open(args[2]).read()        #args[2] is the name of the src_one.
                                         #we open the input file, read it, and save into a variable

    input_text = src_one + src_two    # combined text_source
    ngram = int(args[3])                 # args[3] represents the desired tuple size
    
    ######################### Run program #############################################
    chain_dict = make_chains(input_text, ngram)
    random_text = make_text(chain_dict)
    print random_text, len(random_text)

if __name__ == "__main__":
    main()

