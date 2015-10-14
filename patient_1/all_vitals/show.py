import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter as sc 

train_vitals = pd.read_csv('~/xerox_parc/tryin/Training_Dataset/id_time_vitals_train.csv')

for j in range(1, 3595):
    a = train_vitals[train_vitals['ID'] == j]
    
    plt.clf()
    plt.figure(1)
    plt.subplot(6, 1, 1)
    plt.plot(a['TIME'], a['V1'])
    plt.subplot(6, 1, 2)
    plt.plot(a['TIME'], a['V2'])
    plt.subplot(6, 1, 3)
    plt.plot(a['TIME'], a['V3'])
    plt.subplot(6, 1, 4)
    plt.plot(a['TIME'], a['V4'])
    plt.subplot(6, 1, 5)
    plt.plot(a['TIME'], a['V5'])
    plt.subplot(6, 1, 6)
    plt.plot(a['TIME'], a['V6'])
    plt.savefig('patient_' + str(j) + '.png')
