#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0

# To vectorise the data we assign Sara = 0 and Chris = 1
for vectorised_name, from_person in [(0, from_sara), (1, from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            parsed_email = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            parsed_email = parsed_email.replace('sara', '')
            parsed_email = parsed_email.replace('shackleton', '')
            parsed_email = parsed_email.replace('chris', '')
            parsed_email = parsed_email.replace('sshacklensf', '')
            parsed_email = parsed_email.replace('cgermannsf', '')

            # The idea of stemming is to improve IR performance generally by
            # bringing under one heading variant forms of a word which share a
            # common meaning. Stemming is not a concept applicable to all
            # languages. It is not, for example, applicable in Chinese. But to
            # languages of the Indo-European group, a common pattern of word
            # structure does emerge.
            #
            # Prefixes may be added on the left of words. So unhappiness has a
            # prefix un, a suffix ness, and the y of happy has become i with
            # the addition of the suffix. Usually, prefixes alter meaning
            # radically, so they are best left in place (German and Dutch ge is
            # an exception here). But suffixes can, in certain circumstances,
            # be removed. So for example happy and happiness have closely
            # related meanings, and we may wish to stem both forms to happy, or
            # happi. Infixes can occur, although rarely: ge in German and
            # Dutch, and zu in German.
            #
            # The Snowball stemmer accounts for prefixes and suffixes of words
            # and constitutes a common stem for them. So the stem for 'happy'
            # and 'happiness' is 'happi'. This idea is extended to include
            # proper nouns and places where common nouns wouldn't have suffixes
            # (e.g Germany).
            parsed_email = parsed_email.replace('germani', '')

            ### append the text to word_data
            word_data.append(parsed_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            from_data.append(vectorised_name)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

print word_data[152]

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit_transform(word_data)

vocab_list = vectorizer.get_feature_names()
print len(vocab_list)
print vocab_list[34597]
