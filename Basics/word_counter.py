'''
    Author: Nebiyou Yismaw

    This is a python code that counts words in a text and returns a dictionary
    of list of words with their frequency
'''

import re
from collections import Counter

"""
    Count words.
"""
def word_counter(text):
    counts = dict()  # dictionary of words with their frequency
    # let's convert the text to lower case
    lower_txt = text.lower()
    # Now lets Split text into tokens (words), leaving out punctuation
    # We will use [^0-9a-zA-Z] regex to get and split on non-alphanumeric chars
    # from the tokens let's get counts of each word using Counter from collections
    tokens = re.split('[^0-9a-zA-Z]',text)
    # using dict() let's convert the Counter object to a dict
    counts = dict(Counter(tokens))
    return counts
