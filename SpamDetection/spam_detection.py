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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection  import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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
    pprint.pprint(bag_of_words_naive)
    # now let's use scikit-learn's bag of words
    # let's split our data to train test
    X_train, X_test, y_train, y_test = train_test_split(data_frame['sms_message'],
                                                        data_frame['label'],
                                                        random_state=1)
    print('Number of rows in the total set: {}'.format(data_frame.shape[0]))
    print('Number of rows in the training set: {}'.format(X_train.shape[0]))
    print('Number of rows in the test set: {}'.format(X_test.shape[0]))
    # create a countvecotrizer object using our documents list
    count_vector = CountVectorizer()
    # Now let's build our traning and testing dataset
    # Fit the training data and then return the matrix
    training_data = count_vector.fit_transform(X_train)
    # Transform testing data and return the matrix. Note we are not fitting
    # the testing data into the CountVectorizer()
    testing_data = count_vector.transform(X_test)
    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_data, y_train)
    predictions = naive_bayes.predict(testing_data)
    print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
    print('Precision score: ', format(precision_score(y_test, predictions)))
    print('Recall score: ', format(recall_score(y_test, predictions)))
    print('F1 score: ', format(f1_score(y_test, predictions)))




if __name__ == "__main__":
    main(sys.argv)
