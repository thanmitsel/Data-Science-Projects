#!/usr/bin/python

import pandas as pd

#Module with functions to manipulate files
import manipulate_files
import fraud_simulation

# Reads .txt files
data=manipulate_files.read_files()
print('Files read')
# Sorts the files in order to be space relevant
data=manipulate_files.sort_files(data)
print('Files sorted')
# Finds consumers with full data for a year
# Output: index MeterID consumers vs halfhours of a year
timeseries=manipulate_files.find_full_values(data)
print('Dataset formated to annual data')
# Applies types of attack
# Outputs X and Y with MeterID index
X, Y=fraud_simulation.typical_attack(timeseries)
print('Fraud Simulation done')
print(timeseries)
