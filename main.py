import pandas as pd

df = pd.DataFrame([
    [1, 'Hangzhou',  2000, ],
    [2, 'Shanghai',  4000, ],
    [3, 'Beijing',   5000, ],
    [4, 'Guangdong', 3000, ],
    [5, 'Shenzhen',  5000, ],
    [6, 'Nanjing',   2000, ],
],
    columns=['city id', 'city name', 'average salary'])

df = pd.DataFrame({
    'city id': [1, 2, 3, 4, 5, 6, ],
    'city name': ['Hangzhou', 'Shanghai', 'Beijing',  'Guangdong', 'Shenzhen', 'Nanjing', ],
    'average salary': [2000, 4000, 5000, 3000, 5000, 2000, ],
})
print(df)
# print(df.head(1))
print(df.iloc[0:2])
print(df.iloc[0, 2])
print(df.iloc[0, 1])
