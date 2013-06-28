#!/usr/bin/env python
#Hackbright exercise 8
# 6.27.13

import sys
import random


def make_chains(corpus): #n is the n-gram of the markov chain
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # start with a string = corpus
    
    words = corpus.split() # w is a list = [a, quick, brown, fox]
    # loop through and return all adjacent pairs of words -> keys
    # word that follows each key -> value


    length_of_wordlist = range(len(words)-2) 
    #r is a list of positions = [0,1,2]. we subtract 2 because the last pair has no match


    chains = {}  #this is our empty chains dictionary

    for i in length_of_wordlist:
        key = (words[i], words[i +1])  #key is pairs of words in text
        value = words[i +2]            # value is the next word that follows the key
        
        if chains.get(key, None):
            chains[key].append(value)    # if key exist do smthg, else return None which make stmt false and go to else stmt
        else:
            chains[key] = [value]       # add a new key, value  pair

    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
                                            

    text_list = []                        # this is a list

    ##############this chooses a random key. Only once in the program
    current_key = random.choice(chains.keys()) 
    text_list.append(current_key[0])
    text_list.append(current_key[1])
   
    ############################### below this line is the loop

    while chains.get(current_key, None):
        len_value_list = len(chains[current_key])       # how many value exist for the current key
        value_list = chains[current_key]                # list of all value for each key
         
        random_value = random.randint(0,len_value_list-1) # computation to pick a random item in value
        

        text_list.append(value_list[random_value])          # adding random value to list
        

        current_key = (current_key[1], value_list[random_value]) # reassign current key with new pair
        

    return " ".join(text_list)


def main():
    args = sys.argv             # args is the list (markov.py, inputfile)

    input_text = open(args[1]).read()    #args[1] is the name of the inputfile.
                                        # we open the input file, read it into a string called input_file

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()


