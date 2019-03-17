import pandas as pd

fifa = pd.read_csv('data.csv' , index_col=0)

#question-1
print(fifa.loc[10:20, ['Name', 'Nationality', 'Club', 'Value']])

#question -2
print(fifa[fifa.Club=='Chelsea'].loc[ :, ['Name', 'Nationality', 'Value']])

#question-3
print(fifa[(fifa.Club=='Chelsea') &(fifa.Potential > 90)].loc[ :, ['Name', 'Nationality', 'Value']])

#question-4
print((fifa[(fifa.Club=='Chelsea')].Potential.sum()))

#question-5
print((fifa[(fifa.Club=='Chelsea') &(fifa.Potential > 90)].Potential.sum()))

#question-6
print(fifa[fifa.Position == 'GK'].groupby('Nationality').Nationality.count().sort_values(ascending=False))

#question-7
accepted_columns =['Name','Nationality','Value','Potential']
potential_mean = fifa.Potential.mean()
for column in fifa:
    if column not in accepted_columns:
        fifa=fifa.drop(column, axis = 1)
fifa['GoodBuy'] = fifa.Potential.apply(lambda x: True if x >=potential_mean else False)
print(fifa.head())
