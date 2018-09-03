import pandas as pd
import numpy as np
import random
#from sklearn.model_selection import train_test_split

def typical_attack(timeseries):
    # Applys typical attack to a perc of consumers
    fraud_rate=0.1
    intensity=1-np.random.beta(6,3)
    mal_idx=timeseries.sample(frac=fraud_rate).index
    
    # Y dataframe with index the MeterID
    listofzeros=[0]*len(timeseries)
    Y=pd.DataFrame(listofzeros)
    Y.index=timeseries.index
    Y.loc[mal_idx]=1
    
    # Loop for every malicious MeterID
    end=len(timeseries.columns)
    for i in mal_idx:
        intr_fraud=random.choice(range(0, end, 1))
        while intr_fraud>= end or intr_fraud<=0:
            intr_fraud=random.choice(range(0, end, 1))
            timeseries[i].iloc[intr_fraud:end]=timeseries[i].iloc[intr_fraud:end]*intensity
    
    return timeseries, Y
    
def test_loop(timeseries):
    intensity=1-np.random.beta(6,3)
    mal_idx=timeseries.sample(frac=0.1).index
    end=len(timeseries.columns)
    for i in mal_idx:
        intr_fraud=random.choice(range(0, end, 1))
        while intr_fraud>= end or intr_fraud<=0:
            intr_fraud=random.choice(range(0, end, 1))
            timeseries[i].iloc[intr_fraud:end]=timeseries[i].iloc[intr_fraud:end]*intensity
    return timeseries
    
