__author__ = 'jalFaizy, ashishmokalkar79, mybestthings'

# import csv
# import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score as ac
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

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
    print "read files"
    # train_labs_vitals = pd.DataFrame.merge(train_vitals, train_labs, on='ID')
    # train_age_labs_vitals = pd.DataFrame.merge(train_age_labs, train_vitals, on='ID')
    
    train_all = pd.concat([train_age, train_labs, train_vitals, train_label], axis = 1)
    print "concated"
    
    train_all = train_all.fillna(value = 0)
    
    train_x_all = train_all[['ID', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18', 'L19', 'L20', 'L21', 'L22', 'L23', 'L24', 'L25', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'AGE']].values
    train_y_all = train_all.LABEL.values
    print "trained"
    
    train_x, test_x, train_y, test_y = train_test_split(train_x_all, train_y_all, test_size = 0.40, random_state = 42)
    print "split"
    
    """
    clf = KNeighborsClassifier(n_neighbors=3)
    clf = clf.fit(train_x, train_y)
    prediction = clf.predict(test_x)
    # not running!
    """
    
    """
    clf = SVC(kernel = "sigmoid")
    clf = clf.fit(train_x, train_y)
    prediction = clf.predict(test_x)
    # acc : 99.69
    """
    
    """
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(train_x, train_y)
    prediction = clf.predict(test_x)
    # 99.98
    """
    
    """
    clf = RandomForestClassifier(n_estimators=1000)
    clf = clf.fit(train_x, train_y)
    prediction = clf.predict(test_x)
    # taking too much time
    """
    
    """
    clf = RandomForestClassifier(n_estimators=100)
    clf = clf.fit(train_x, train_y)
    prediction = clf.predict(test_x)
    # 99.99
    """
    
    # print ac(test_y, prediction)

def main():
    first_csv_file=sys.argv[1];
    second_csv_file=sys.argv[2];
    third_csv_file=sys.argv[3];
    
    # test_vitals, test_labs, test_age = read_args(first_csv_file, second_csv_file, third_csv_file)
    # test_all = preprocess(test_vitals, test_labs, test_age)
    trainer()

main()
