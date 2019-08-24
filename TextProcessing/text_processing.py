'''
    Author: Nebiyou Yismaw

    This is a python code that will request a webpage and clean it to get a
    certain text.
'''

import requests
import re
from bs4 import BeautifulSoup
import sys
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.corpus import stopwords

def normalization(text):
    '''
        This function will normalize a string. These include chaning to lower
        case, remove special characters or punctuations.
    '''
    # convert to lower and replace anything that is not with in [a-z], [A-Z] or
    # [0-9] by a space
    # It's better to replace punctuations with space as opposed to a blank
    return re.sub(r"[^a-zA-Z0-9]", " ", text.lower())

def tokenize_words(text):
    '''
        This function splits texts into a list of words
    '''
    return word_tokenize(text)

def tokenize_sentences(text):
    '''
        This function splits texts into a list of sentences
    '''
    return sent_tokenize(text)

def stop_words_remove(text):
    '''
        This function removes what are cold stop words. These are uninformative
        words like is are was ...
    '''
    return [w for w in words if w not in stopwords.words("english")]

def stremming(words):
    '''
        streaming is reducing a word to it's root form. Final word might no
        be an actual word. It doesn't need a dictionary.
    '''
    return [PorterStemmer().stem(w) for w in words]

def Lemmatizing(words):
    '''
        Lemmatizing is reducing a word to it's root form using some sort of
        dictionary

        Lemmatizing can be done to nouns, verbs.
    '''
    return [WordNetLemmatizer().lemmatize(w) for w in words]

def main(argv):
    '''
        @main
    '''
    # request a webpage
    r = requests.get(argv[1])
    # now we have a the entire HTML page
    # print (r.text)
    # let's define a pattern for HTML tags
    patten_html_tags = re.compile(r'<.*?>')
    html_tags_removed = patten_html_tags.sub('',r.text)
    # let's print the text with the tags remvoed
    # print (html_tags_removed)

    # We can see that some scripts and codes exist, meaning parsing wasn't clean
    # let's use beautiful soup to parse HTML
    soup = BeautifulSoup(r.text, "html5lib")
    # get table rows (summaries)  with class athing
    summaries = soup.find_all("tr", class_="athing")
    # Find all articles, extract titles
    # for each summary get an a tag with a storylink class and get
    # the text and strip it
    articles = [ summary.find("a", class_="storylink").get_text().strip() for summary in summaries ]
    print(len(articles), "Article summaries found. Sample:")
    print(articles[0])

if __name__=="__main__":
    main(sys.argv)
