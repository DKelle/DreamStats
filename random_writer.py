from get_dreams import get_dreams
import sys
import re
import random

def sanitize(dreams):
    for i, dream in enumerate(dreams):
        #dream = dream.translate(None, ',!-:;\'"?"()\n')
        dream = dream.lower()
        dreams[i] = dream

    return dreams

def analyze(dreams, anchor_len):
    next_word_dict = {}

    for dream in dreams:
        #First, parse out any punctuation
        words = dream.split()

        for i in range(0, len(words)-anchor_len):
            anchor_list = words[i:i+anchor_len]
            anchor = ' '.join(anchor_list)
            next_word = words[i+anchor_len]

            #keep a list of the words that appear after the ancho
            if anchor not in next_word_dict:
                next_word_dict[anchor] = []
            next_word_dict[anchor].append(next_word)

    return next_word_dict

def get_seed(dreams, anchor_len):
    # Pick a random seed
    dream = random.choice(dreams)

    # Return the first word in this dream
    seed_list = dream.split()[0:anchor_len]
    return ' '.join(seed_list)

def generate_words(seed, next_word_dict, number_to_generate, anchor_len, dreams):
    random_dream = seed + ' '
    done = False
    count = 0
    while not done:
        count = count + 1
        if seed not in next_word_dict:
            # This seed is not in the next_word_dict
            # probably means that this was the last word in a dream
            # End this sentance, and start a new one
            random_dream += '.'
            seed = get_seed(dreams, anchor_len)
        next_word_list = next_word_dict[seed]
        next_word = random.choice(next_word_list)
        random_dream += next_word + ' '

        # Get a new seed
        last_words = random_dream.split()[-anchor_len:]
        seed = ' '.join(last_words)

        # Only stop at the end of sentance
        done = count > number_to_generate and '.' in random_dream.split()[-1]

    return random_dream

if __name__ == "__main__":
    # Get a list of dreams, with no dates
    dreams = get_dreams()

    # parse out punctuation, and lowercase all strings
    dreams = sanitize(dreams)

    # Find out how many words we will use as our anchor
    # eg. [In] = "this"
    # vs  [In this] = "dream"
    anchor_len = int(sys.argv[1])

    # Get the list of words that follow each anchor
    next_word_dict = analyze(dreams, anchor_len)

    # Now that we have our list of probable next words, pick a seed
    seed = get_seed(dreams, anchor_len)
    print 'seed is ' + str(seed)

    # Use the seed to start generating the next words
    random_dream = generate_words(seed, next_word_dict, 100, anchor_len, dreams)

    with open('random_dream.txt', 'w') as f:
        f.write(random_dream)
    print(random_dream)
