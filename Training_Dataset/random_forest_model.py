__author__ = 'jalFaizy, ashishmokalkar79, mybestthings'
import csv

import sys
import os
import pandas as pd

"""
print "FILES"
print first_csv_files;
print second_csv_file;
print third_csv_file;
print fourth_csv_file;

print "FILE: ID_AGE_TRAIN "
with open('id_age_train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

print "FILE: ID_LABEL_TRAIN "

with open('id_label_train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
print "FILE: ID_TIME_LABS_TRAIN "

with open('id_time_labs_train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
print "FILES: ID_TIME_VITALS_TRAIN"

with open('id_time_vitals_train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
"""

def read_args(vitals_train, labs_train, age_train):
    """ 
    This function reads arguments and returns pandas.DataFrame object
    """
    train_vitals = pd.read_csv(vitals_train)
    train_labs = pd.read_csv(labs_train)
    train_age = pd.read_csv(age_train)
    
    """
    # testing 
    print train_age.describe()
    """
    
    return train_vitals, train_labs, train_age

def preprocess(train_vitals, train_labs, train_age):
    """
    This function preprocess data 
    1. equalize
    2. merge dataframes 
    """
    #TODO
    
    """
    # testing 
    print train_age.describe()
    """
    
    return None

def main():
    first_csv_file=sys.argv[1];
    second_csv_file=sys.argv[2];
    third_csv_file=sys.argv[3];
    # fourth_csv_file=sys.argv[4];
    
    train_vitals, train_labs, train_age = read_args(first_csv_file, second_csv_file, third_csv_file)
    train_all = preprocess(train_vitals, train_labs, train_age)

main()
