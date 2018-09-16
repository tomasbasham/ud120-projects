#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)

### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )

### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from time import time

clf = DecisionTreeClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

t0 = time()
accuracy = accuracy_score(labels_test, pred)
print "testing time:", round(time()-t0, 3), "s"

print "accuracy:", accuracy
print

# Discriminant words
discriminant_words = []

feature_importances = clf.feature_importances_
feature_names = vectorizer.get_feature_names()

for i in range(len(feature_importances)):
    if feature_importances[i] > 0.2:
        discriminant_words.append((i, feature_importances[i], feature_names[i]))

# Sort the words by the most important
discriminant_words.sort(key=lambda tup: tup[1])

for feature in discriminant_words:
    print feature[0], feature[1], feature[2]
