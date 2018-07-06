#!/usr/bin/python

"""
    This is the code to accompany the Lesson 4 (Choose Your Own Algorithm)
    mini-project.

    Use a new Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import math

# The number of trees in the forest. The larger the better, but also the longer
# it will take to compute. In addition, note that results will stop getting
# significantly better beyond a critical number of trees.
#
# Changing only this variable I see:
#
# +-----+--------+-------+-------+----------+
# | val | train  | pred  | test  | accuracy |
# +-----+--------+-------+-------+----------+
# | 10  | 4.768  | 0.032 | 0.001 | 99.659   |
# | 20  | 10.382 | 0.04  | 0.001 | 99.545   |
# | 40  | 18.972 | 0.063 | 0.001 | 99.716   |
# | 60  | 29.317 | 0.077 | 0.001 | 99.716   |
# | 80  | 38.023 | 0.089 | 0.001 | 99.658   |
# | 100 | 48.037 | 0.106 | 0.001 | 99.658   |
# +-----+--------+-------+-------+----------+
#
# There seems to be a sweet spot around the 40 mark that yields a good accuracy
# in a good amount of time. Howver due to the random nature of this classifier
# I have ssen accuracy scores both lower and higher (up to 99.78) for a value
# of 80.
n_estimators = 40

# The function to measure the quality of a split. Supported criteria are "gini"
# for the Gini impurity and "entropy" for the information gain. Note: this
# parameter is tree-specific.
criterion = "gini"

# One of the main parameters to tune is the `max_features` parameter. This
# defines the size of the random subsets of features to consider when splitting
# a node. The lower the greater the reduction of variance, but also the greater
# the increase in bias. An empirical good default value is
# `max_features=sqrt(n_features)`
max_features = "auto" # sqrt(n_features)

# Random Forest Classifier
#
# A random forest is a meta estimator that fits a number of decision tree
# classifiers on various sub-samples of the dataset and use averaging to
# improve the predictive accuracy and control over-fitting. The sub-sample size
# is always the same as the original input sample size but the samples are
# drawn with replacement if bootstrap=True (default).
#
# https://medium.com/machine-learning-101/chapter-5-random-forest-classifier-56dc7425c3e1
clf = RandomForestClassifier(n_estimators=n_estimators, max_features=max_features)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

t0 = time()
accuracy = accuracy_score(pred, labels_test)
print "testing time:", round(time()-t0, 3), "s"

print "accuracy:", accuracy
print

# Extra Trees Classifer
clf = ExtraTreesClassifier(n_estimators=n_estimators, max_features=max_features)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

t0 = time()
accuracy = accuracy_score(pred, labels_test)
print "testing time:", round(time()-t0, 3), "s"

print "accuracy:", accuracy

#########################################################
