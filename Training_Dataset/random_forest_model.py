__author__ = 'jalFaizy, ashishmokalkar79, mybestthings'

import csv
import sys
import os
import pandas as pd
import sklearn as sk
from sklearn.metrics import accuracy_score

"""
print "FILES"
print first_csv_files;
print second_csv_file;
print third_csv_file;
print fourth_csv_file;

print "FILE: ID_AGE_test "
with open('id_age_test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

print "FILE: ID_LABEL_test "

with open('id_label_test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
print "FILE: ID_TIME_LABS_test "

with open('id_time_labs_test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
print "FILES: ID_TIME_VITALS_test"

with open('id_time_vitals_test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
"""

def read_args(vitals_test, labs_test, age_test):
    """ 
    This function reads arguments and returns pandas.DataFrame object
    """
    test_vitals = pd.read_csv(vitals_test)
    test_labs = pd.read_csv(labs_test)
    test_age = pd.read_csv(age_test)
    
    """
    # testing 
    print test_age.describe()
    """
    
    return test_vitals, test_labs, test_age

def preprocess(test_vitals, test_labs, test_age):
    """
    This function preprocess data 
    1. equalize
    2. merge dataframes 
    """
    #TODO
    
    """
    # testing 
    print test_age.describe()
    """
    
    """
    /*
test_labs_equi = pd.DataFrame(test_labs[test_labs.ID == 1].mean())
for i in range(2, 3594):
    test_labs_equi = pd.concat([test_labs_equi, test_labs[test_labs.ID == i].mean()], axis = 1)
    
test_labs.equi = test_labs.equi.T
*/
    """    
    return None

def main():
    first_csv_file=sys.argv[1];
    second_csv_file=sys.argv[2];
    third_csv_file=sys.argv[3];
    # fourth_csv_file=sys.argv[4];
    
    test_vitals, test_labs, test_age = read_args(first_csv_file, second_csv_file, third_csv_file)
    test_all = preprocess(test_vitals, test_labs, test_age)

main()
