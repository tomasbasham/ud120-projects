#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

number_of_people = len(enron_data)
print "number of people:", number_of_people

number_of_features = len(enron_data.itervalues().next())
print "number of features:", number_of_features

number_of_pois = len([poi for poi in enron_data.keys() if enron_data[poi]["poi"] == 1])
print "number of POIs:", number_of_pois

# print "\n".join(sorted(enron_data.keys()))

print
print "James Prentice total stock value:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Wesley Colwell emails sent to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeff Skilling exercised stock options:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print
print "Ken Lay total payments:", enron_data["LAY KENNETH L"]["total_payments"]
print "Jeff Skilling total payments:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Andy Fastow total payments", enron_data["FASTOW ANDREW S"]["total_payments"]

print
print len([poi for poi in enron_data.keys() if enron_data[poi]["salary"] != 'NaN'])
print len([poi for poi in enron_data.keys() if enron_data[poi]["email_address"] != 'NaN'])

total_missing_payments = len([poi for poi in enron_data.keys() if enron_data[poi]["total_payments"] == 'NaN'])
print "percentage of people missing total payments:", float(total_missing_payments)/number_of_people * 100.0

pois_missing_payments = len([poi for poi in enron_data.keys() if enron_data[poi]["total_payments"] == 'NaN' and enron_data[poi]["poi"] == 1])
print "percentage of POIs missing total payments:", float(pois_missing_payments)/number_of_pois * 100.0
