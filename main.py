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
print(city_salary)
print(city_list)
print(type(city_salary))
print(type(city_list))
