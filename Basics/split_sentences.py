'''
    Author: Nebiyou Yismaw

    This is a python code that will split a text into sentences and then to
    words
'''

import re


def remove_spaces(list_of_txts):
    '''
        This function to remove trailing and leading white spaces from a list
        of texts and returns the cleaned up list (members that aren't empty)
    '''
    return [ txt.strip() for txt in list_of_txts if txt.strip() ]


def sent_tokenize(text):
    """Split text into sentences."""
    #
    # Split text by sentence delimiters (remove delimiters)
    #
    tokens = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',text)
    # return tokens wih removed white spaces
    return remove_spaces(tokens)


def word_tokenize(sent):
    """Split a sentence into words."""

    tokens = re.split('[^0-9a-zA-Z]',sent)
    # return tokens wih removed white spaces
    return remove_spaces(tokens)
