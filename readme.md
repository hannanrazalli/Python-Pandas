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


grade_data = {
    "A":4,
    "B":3.5,
    "C":3,
    "D":2.5
}
grade = pd.Series(grade_data)
print(grade)