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
    'Grade' : grade_data,
    'Marks' : marks_dict
})

df['ScaledMarks'] = (df['Marks']/90*100).round(1)

print(df)