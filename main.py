import pandas as pd

df = pd.DataFrame([
    [1, 'Hangzhou', 2000],
    [2, 'Shanghai', 4000],
    [3, 'Beijing', 5000],
    [4, 'Guangdong', 3000],
    [5, 'Shenzhen', 5000],
    [6, 'Nanjing', 2000],
],
                  columns=['city id', 'city name', 'lowest salary'])

print(df)
