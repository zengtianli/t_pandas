import pandas as pd

df = pd.read_csv('employee.csv')
# print(df)

# df['mood'] = ['happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy',
#               'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', ]
# df['mood'] = df.company.apply(lambda x: 'happy' if x == 'Uber' else 'unhappy')
# df['MOOD'] = df['mood'].apply(lambda x: x.upper())
# df['total_wage'] = df.apply(
#     lambda x: x.hours_worked*x.hourly_wage, axis='columns')
# df['total_wage'] = df['hourly_wage']*df['hours_worked']

df.columns = ['column 1', 'column 2', 'column 3',
              'column 4', 'column 5', 'column 6', ]
df = df.rename(columns={'id': 'ID'})
df = df.rename(str.upper, axis=1)
print(df)
print(df.info())
