from get_dreams import get_dreams
import sys
import re
import random

def analyze(dreams, anchor_len):
    next_word_dict = {}

    for dream in dreams:
        #First, parse out any punctuation
        dream = dream.translate(None, '.,!-:;\'"?"()\n')
        words = dream.split()

        for i in range(0, len(words)-anchor_len):
            anchor_list = words[i:i+anchor_len]
            anchor = ' '.join(anchor_list).lower()
            next_word = words[i+anchor_len].lower()

            #keep a list of the words that appear after the ancho
            if anchor not in next_word_dict:
                next_word_dict[anchor] = []
            next_word_dict[anchor].append(next_word)

    return next_word_dict

def get_seed(dreams):
    # Pick a random seed
    dream = random.choice(dreams)

    # Return the first word in this dream
    return dream.split()[0]

if __name__ == "__main__":
    # Get a list of dreams, with no dates
    dreams = get_dreams()

    # Find out how many words we will use as our anchor
    # eg. [In] = "this"
    # vs  [In this] = "dream"
    anchor_len = int(sys.argv[1])

    # Get the list of words that follow each anchor
    next_word_dict = analyze(dreams, anchor_len)

    # Now that we have our list of probable next words, pick a seed
    seed = get_seed(dreams)

