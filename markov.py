#!/usr/bin/env python
#Hackbright exercise 8
# 6.27.13

import sys


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # start with a string = corpus
    
    words = corpus.split() # w is a list = [a, quick, brown, fox]
    # loop through and return all adjacent pairs of words -> keys
    # word that follows each key -> value


    length_of_wordlist = range(len(words)-2) 
    #r is a list = [0,1,2]. we subtract 2 because the last pair has no match


    d_chain = {}  #this is our empty chains dictionary

    for i in length_of_wordlist:
        key = (words[i], words[i +1])  #key is pairs of words in text
        value = words[i +2]            # value is the next word that follows the key
        
        if d_chain.get(key, None):
            d_chain[key].append(value)       
        else:
            d_chain[key] = [value]

    #print d_chain

    return d_chain

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

# def main():
#     args = sys.argv             # input is make_chains(corpus)

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()


# s= """
# I do not like them
# in a house.
# I do not like them
# with a mouse.
# I do not like them
# here or there.
# I do not like them
# anywhere.

# """

# make_chains(s)
