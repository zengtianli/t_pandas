1 made own dataframe 2 method 
# 1 dataframe, head iloc,info
## 1.1 method 1
```python

df = pd.DataFrame([
    [1, 'Hangzhou',  2000, ],
    [2, 'Shanghai',  4000, ],
    [3, 'Beijing',   5000, ],
    [4, 'Guangdong', 3000, ],
    [5, 'Shenzhen',  5000, ],
    [6, 'Nanjing',   2000, ],
],
    columns=['city id', 'city name', 'average salary'])
```
## 1.2 method 2
```python
df = pd.DataFrame({
    'city id': [1, 2, 3, 4, 5, 6, ],
    'city name': ['Hangzhou', 'Shanghai', 'Beijing',  'Guangdong', 'Shenzhen', 'Nanjing', ],
    'average salary': [2000, 4000, 5000, 3000, 5000, 2000, ],
})
```

## vim macro

# 2 part of dataframe

```python
city_list = df.city_name
city_list = df['city_name']
city_salary = df[['city_name', 'average salary']]
print(type(city_salary))
print(type(city_list))
```

## 3 head iloc info type

2 head() iloc index location
