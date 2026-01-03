import pandas as pd

marks_dict = ({
  'A' : 85,
  'B' : 75,
  'C' : 65,
  'D' : 55
})

grade_dict = ({
  'A' : 4,
  'B' : 3.5,
  'C' : 3,
  'D' : 2.5
})

mark = pd.Series(marks_dict)
grade = pd.Series(grade_dict)

df = pd.DataFrame({
    'Marks' : mark,
    'Grades' : grade
})

print(df.iloc[1])