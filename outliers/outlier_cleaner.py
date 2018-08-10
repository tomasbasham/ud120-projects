#!/usr/bin/python

from itertools import izip

def outlierCleaner(predictions, ages, net_worths, percent=0.9):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # Create the tuples that will be returned from the function.
    for prediction, age, net_worth in izip(predictions, ages, net_worths):
        cleaned_data.append((age, net_worth, abs(prediction - net_worth)))

    # sort the list of tuples by the error.
    cleaned_data.sort(key=lambda x: x[2])

    # Strip away 10% of the data having the largest residual error.
    ninty_percent = int(len(cleaned_data) * percent)
    return cleaned_data[:ninty_percent]
