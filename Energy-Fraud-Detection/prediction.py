import pandas as pd
import numpy as np
import sys
from time import time
# Import SVM from LibLinear
#sys.path.insert(0,'/opt/liblinear-2.20/python')
#from liblinearutil import *

# Import SVM from sklearn with the same algorithm
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def liblinear(X, Y):
    #Linear SVM function with sklearn
    
    # Split data
    X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.33)
    
    # Training-Testing
    clf = LinearSVC()
    #t0=time()
    clf.fit(X_train, Y_train)
    #print("done in %0.3fs" % (time()-t0))
    prediction=clf.predict(X_test)
    
    # Conver to list
    pred_list=prediction.tolist()
    y_list=Y_test[0].tolist()

    # Confusion matrix, Results
    tn, fp, fn, tp=confusion_matrix(y_list, pred_list).ravel()
    print(classification_report(y_list, pred_list))
    print(confusion_matrix(y_list, pred_list))
    return 

