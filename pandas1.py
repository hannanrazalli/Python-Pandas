import pandas as pd

A = pd.Series(['a','b','c'], index = [1,3,5])

print(A.loc[1:3])
print(A.iloc[1:3])