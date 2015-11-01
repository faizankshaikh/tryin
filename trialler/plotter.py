import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix as cfm
from sklearn.metrics import classification_report as clr

pred_arr = np.array([])
real_df = pd.read_csv('id_label_val.csv')
pred_df = pd.read_csv('output.csv')    
real_arr = real_df.LABEL.values    
for i in range(3595, 4793):
    temp1 = pred_df[pred_df.ID == i]
    if len(temp1[temp1.LABEL == 1]) > 0:
        pred_arr = np.append(pred_arr, 1)        
    else:
        pred_arr = np.append(pred_arr, 0)

fpr, tpr, _ = roc_curve(real_arr, pred_arr)
roc_auc = auc(fpr, tpr)

# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

# conf matrix
print cfm(real_arr, pred_arr)
# print clr(real_arr, pred_arr)
