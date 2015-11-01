__author__ = 'jalFaizy, ashishmokalkar79, mybestthings'

import sys
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold

def read_args(vitals_test, labs_test, age_test):
    """ 
    This function reads arguments and returns pandas.DataFrame object
    """
    test_vitals = pd.read_csv(vitals_test)
    test_labs = pd.read_csv(labs_test)
    test_age = pd.read_csv(age_test)
        
    return test_vitals, test_labs, test_age


def trainer():
    '''
    This function trains model and returns it along with filler
    '''
    train_age = pd.read_csv('id_age_train.csv')
    train_label = pd.read_csv('id_label_train.csv')
    train_labs = pd.read_csv('id_time_labs_train.csv')
    train_vitals = pd.read_csv('id_time_vitals_train.csv')
    
    val_age = pd.read_csv('id_age_val.csv')
    val_label = pd.read_csv('id_label_val.csv')
    val_labs = pd.read_csv('id_time_labs_val.csv')
    val_vitals = pd.read_csv('id_time_vitals_val.csv')
    
    
    train_age_labs = pd.merge(train_age, train_labs, on='ID')
    train_age_labs_vitals = pd.merge(train_age_labs, train_vitals, on = ['ID', 'TIME'])
    training_all = pd.merge(train_age_labs_vitals, train_label, on = 'ID')
    
    val_age_labs = pd.merge(val_age, val_labs, on='ID')
    val_age_labs_vitals = pd.merge(val_age_labs, val_vitals, on = ['ID', 'TIME'])
    val_all = pd.merge(val_age_labs_vitals, val_label, on = 'ID')
    
    train_all = pd.concat([training_all,val_all])

    filler =  train_all[(train_all['ICU'] == 0) & (train_all['LABEL'] == 0)].mean() * 1.25
    train_all.iloc[0] = train_all.iloc[0].fillna(filler)
    
    temp = train_all[train_all.ID == 1]
    
    for i in range(2, 4793):    
        print (i)
        temp1 = train_all[train_all.ID == i]
        temp1.iloc[0] = temp1.iloc[0].fillna(filler)
        temp = temp.append(temp1, ignore_index = True)
        
    print ("replaced")
    
    
    temp.fillna(method = 'ffill', inplace = True)
    
    train_x = temp[['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L15', 'L16', 'L18', 'L19', 'L20', 'L21', 'L22', 'L23', 'L25', 'V1','V2', 'V3', 'V4', 'V5', 'V6']].values
    train_y = temp.LABEL.values
    
    clf = RandomForestClassifier(n_estimators=30, n_jobs=-1, max_features=1)
    clf = clf.fit(train_x, train_y)

    return clf, filler
    
def tester(modeller, filler, test_vitals, test_labs, test_age):
    '''
    This function tests the model and returns prediction(csv) file
    '''
    test_age_labs = pd.merge(test_age, test_labs, on='ID')
    test_all = pd.merge(test_age_labs, test_vitals, on = ['ID', 'TIME'])
    
    test_all = test_all[test_all.ICU == 1]
    test_all.iloc[0] = test_all.iloc[0].fillna(filler)
    temp = test_all[test_all.ID == 4793]
    
    for i in range(4794, 5991):
        print (i)
        temp1 = test_all[test_all.ID == i]
        temp1.iloc[0] = temp1.iloc[0].fillna(filler)
        temp = temp.append(temp1, ignore_index = True)
    
    temp.fillna(method = 'ffill', inplace = True)
    
    test_x = temp[['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L15', 'L16', 'L18', 'L19', 'L20', 'L21', 'L22', 'L23', 'L25', 'V1','V2', 'V3', 'V4', 'V5', 'V6']].values

    prediction = modeller.predict(test_x)
        
    output = test_all[['ID', 'TIME']]
    output = output.set_index('ID')
    output['LABEL'] = prediction
    
    output.to_csv('output.csv')
        
    return None    

def main():
    first_csv=sys.argv[1];
    second_csv=sys.argv[2];
    third_csv=sys.argv[3];
    
    test_vitals, test_labs, test_age = read_args(first_csv, second_csv, third_csv)
    print ("read args")
    
    modeller, filler = trainer()
    print ("trained")
    
    tester(modeller, filler, test_vitals, test_labs, test_age)
    print ("tested")
    
main()
