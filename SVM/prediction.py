import pandas as pd
import numpy as np
import sys

# Import SVM from LibLinear
#sys.path.insert(0,'/opt/liblinear-2.20/python')
#from liblinearutil import *

# Import SVM from sklearn with the same algorithm
from sklearn.svm import LinearSVC

def liblinear(X):
    clf = LinearSVC()
    return 

