import pandas as pd

df = pd.DataFrame([
    [1, 'Hangzhou',  2000, ],
    [2, 'Shanghai',  4000, ],
    [3, 'Beijing',   5000, ],
    [4, 'Guangdong', 3000, ],
    [5, 'Shenzhen',  5000, ],
    [6, 'Nanjing',   2000, ],
],
    columns=['city id', 'city_name', 'average salary'])

city_list = df.city_name
city_list = df['city_name']
city_salary = df[['city_name', 'average salary']]

# print(city_salary.info())
# print(type(city_salary))
# print(city_list.head())
# print(city_list.iloc[1])

# print(type(city_salary.iloc[1]))

hz = df[df.city_name == 'Hangzhou']
hznj = df[(df.city_name == 'Hangzhou') | (df.city_name == 'Nanjing')]
hznj = df[df.city_name.isin(['Hangzhou', 'Nanjing'])]
hznj.reset_index(inplace=True, drop=True)
hznj.reset_index(inplace=True)
hznj1 = hznj.reset_index()

print(hznj)

print(hznj1)
