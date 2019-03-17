import pandas as pd

#Solution for question_1
df1 = pd.DataFrame({'PG': ['COMP9331', 'COMP9021', 'COMP9024', 'COMP9101'],
                    'UG': ['COMP3121', 'COMP1511', 'COMP3141', 'COMP1531']}
                   )
df1.head


#Solution for question 2
df2 = pd.read_csv('mini_exercise.csv', index_col=0)
##edit this path according to file path
print(df2.head())
df2 = df2.T
df2.to_csv('mini_solution.csv')
