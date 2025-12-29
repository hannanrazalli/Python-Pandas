import pandas as pd

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