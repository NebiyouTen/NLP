'''
    Author: Nebiyou Yismaw

    This is a python code that will different utility functions for the spam
    detector.


'''

import sys
import string
from collections import Counter
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('../TextProcessing')

from text_processing import tokenize_words

def bag_of_words(document):
    '''
        This function will build a bag of words given a document.
    '''
    # first step is to convert all words in our docuemnt to lower case
    lower_case_doc = [ d.lower() for d in document]
    # next step is to remove punctuations
    table = str.maketrans({key: None for key in string.punctuation})
    sans_punctuation_documents = [ s.translate(table) for s in lower_case_doc ]
    # now lets tokenize strings
    preprocessed_documents = [ tokenize_words(s) for s in sans_punctuation_documents ]
    frequency_list = [ Counter(i) for i in preprocessed_documents ]
    return frequency_list
