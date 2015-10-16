__author__ = 'jalFaizy, ashishmokalkar79, mybestthings'

# import csv
# import os
import sys
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import accuracy_score as ac
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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

def trainer():
    train_age = pd.read_csv('id_age_train.csv')
    train_label = pd.read_csv('id_label_train.csv')
    train_labs = pd.read_csv('id_time_labs_train.csv')
    train_vitals = pd.read_csv('id_time_vitals_train.csv')
    
    # train_labs_vitals = pd.DataFrame.merge(train_vitals, train_labs, on='ID')
    # train_age_labs_vitals = pd.DataFrame.merge(train_age_labs, train_vitals, on='ID')
    
    train_all = pd.concat([train_age, train_labs, train_vitals, train_label], axis = 1)
    
    train_all = train_all.fillna(value = 0)
    
    print train_all.head()
    '''
    nn = KNeighborsClassifier(n_neighbors = 3)
    _nn = nn.fit(train_x, train_y)
    prediction = _nn.predict(test_x)
    
    print ac(test_y, prediction)
    '''

def main():
    first_csv_file=sys.argv[1];
    second_csv_file=sys.argv[2];
    third_csv_file=sys.argv[3];
    
    # test_vitals, test_labs, test_age = read_args(first_csv_file, second_csv_file, third_csv_file)
    # test_all = preprocess(test_vitals, test_labs, test_age)
    trainer()

main()
