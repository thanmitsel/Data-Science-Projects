import pandas as pd
import numpy as np

def read_files():
    # Read files from directory and append them 
    data1=pd.read_csv('../../CerData/File1.txt', sep=" ", header=None)
    data2=pd.read_csv('../../CerData/File2.txt', sep=" ", header=None)
    #data3=pd.read_csv('../../CerData/File3.txt', sep=" ", header=None)
    #data4=pd.read_csv('../../CerData/File4.txt', sep=" ", header=None)
    #data5=pd.read_csv('../../CerData/File5.txt', sep=" ", header=None)
    #data6=pd.read_csv('../../CerData/File6.txt', sep=" ", header=None)
    data=data1.append(data2)
    #data=data.append(data3)
    #data=data.append(data4)
    #data=data.append(data5)
    #data=data.append(data6)
    data.columns=['MeterID', 'Timecode', 'Consumption']
    return data

def sort_files(data):
    # Sort files based on their Timecode and MeterID
    data=data.sort_values(by=['MeterID','Timecode'])
    return data.reset_index(drop=True)

def find_full_values(data):
    # Find consumers with data for a full year
    reduced_data=data[data["Timecode"]==73048].index
    ID=[]
    initialize=1
    for i in range(0, len(reduced_data)):
        if (data["Timecode"].iloc[reduced_data[i]-17519]==36601):
            if initialize==1:
                df=data["Consumption"].iloc[(reduced_data[i]-17519):reduced_data[i]+1]
                df=df.reset_index(drop=True)
                initialize=initialize+1
            else:
                df=pd.concat([df, data["Consumption"].iloc[reduced_data[i]-17519:reduced_data[i]+1].reset_index(drop=True)], axis=1)
            ID.append(data["MeterID"].iloc[reduced_data[i]])
    df.columns=ID
    df=df.transpose()
    return df
