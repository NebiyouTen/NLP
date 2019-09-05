'''
    Author: Nebiyou Yismaw

    This is a python code that will naive-bayes algorithm to do a simple spam
    detection. It uses a dataset from the UCI Machine Learning repository,
    which can be found https://archive.ics.uci.edu/ml/machine-learning-databases/00228/.


'''

import sys
import pandas as pd
import numpy as np
from utils import *
import pprint

def main(argv):
    '''
        @main
    '''
    # let's read the data to a pandas data frame
    # The data is tab separated, read the label and the sms message
    data_frame = pd.read_table("SMSSpamCollection", header=None, names=[
                               'label', 'sms_message'])
    # convert labels to binary flag (ham=0 and spam=1)
    data_frame['label'] = data_frame.label.map({"ham": 0, "spam": 1})
    print(data_frame.head(), "\n", data_frame.shape)
    documents = ['Hello, how are you!',
                 'Win money, win from home.',
                 'Call me now.',
                 'Hello, Call hello you tomorrow?']
    bag_of_words_naive = bag_of_words(documents)
    pprint.pprint(bag_of_words_naive
    )


if __name__ == "__main__":
    main(sys.argv)
