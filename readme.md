#First step: Install pandas library - pip install pandas


**TO READ CSV FILE: 
    pd.read_csv('xxx.csv') or pd.read_csv('xxx.csv', index_col='Word')


    df.info()
    df.shape() -- Show size of matrix

    df.loc["xxxxxxxxxxxx] -- Show value of "xxxxxxxxxxxx"
    df.loc[INDEX, COLUMN] -- eg: df.loc["xxxxxxxxxxxx", "VALUE"]

    df = pd.series([0.25,0.5,0.75,1.0], index['a','b','c','d'])

    a = pd.Series([2,3,4,5], index=['a','b','c','d'])
print(type(a.values))
print(type(a))
print(a.index)
print(a['a'])
print(a['a':'c'])

staff = {
    "nama"  : ["Ali","Abu","Ahmad"],
    "umur"  : ["25","26","27"],
    "kerja" : ["analyst","data","engineer"]
}

df = pd.DataFrame(staff)
print(df)

--PRINT pd.Series
grade_data = {
    "A":4,
    "B":3.5,
    "C":3,
    "D":2.5
}
grade = pd.Series(grade_data)
print(grade)


--PRINT VALUE ONLY:
    marks_dict = {
    "A":85,
    "B":75,
    "C":65,
    "D":55
}
marks = pd.Series(marks_dict)
print(marks.values)


marks_dict = {
    "A":85,
    "B":75,
    "C":65,
    "D":55
}
marks = pd.Series(marks_dict)
print(marks['A':'C']) -- EXPLICIT INDEX
print(marks[0:2]) -- IMPLICIT INDEX

--COMBINE 2 SERIES TO BECOME 1 DATAFRAME
import pandas as pd

grade_data = {
    "A":4.0,
    "B":3.5,
    "C":3.0,
    "D":2.5
}

marks_dict = {
    "A":85,
    "B":75,
    "C":65,
    "D":55
}

grade = pd.Series(grade_data)
marks = pd.Series(marks_dict)

df = pd.DataFrame({
    'Marks': marks,
    'Grade': grade}) -- Same as making new dict
print(df)
print(df.T) -- TRANSPOSE

print(df.iloc[0:2]) -- IMPLICIT(FOR NUMBERS)
print(df.loc['A':'C']) - EXPLICIT(FOR LETTERS)

print(df.to_numpy()) -- values change to to_numpy()

-- Added new column
df['% Marks'] = ((df['Marks']/90)*100).round(1)
print(df)

del df['% Marks']

a = df[df['Marks'] > 70]

-- Ada dalam list ada 2 set. Setiap 1 set terletak pada 1 baris
a = pd.DataFrame([ 
    {'a' : 1, 'b' : 2},
    {'b' : 3, 'c' : 4}
    ])


print(a.fillna(0))