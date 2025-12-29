#First step: Install pandas library - pip install pandas

import pandas as pd

#df = pd.read_csv('xxx.csv') # Load data from a CSV file into a DataFrame

#print(pd.__version__) # Print the version of pandas library

a = [1, 7, 2]
myvar = pd.Series(a) # Create a pandas Series from a list
print(myvar) # Print the Series