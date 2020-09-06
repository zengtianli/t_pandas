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

# 3 head iloc info type
```python

print(city_list.head())
print(city_salary.iloc[1:3])
print(city_salary.iloc[1,2])
print(city_salary.head())
print(city_salary.info())
print(city_list.iloc[1])
print(city_salary.iloc[1])
```

# 4 df logic operation
```python
hz = df[df.city_name == 'Hangzhou']
hznj = df[(df.city_name == 'Hangzhou') | (df.city_name == 'Nanjing')]
hznj = df[df.city_name.isin(['Hangzhou', 'Nanjing'])]
hznj.reset_index(inplace=True, drop=True)
hznj.reset_index(inplace=True)
hznj1 = hznj.reset_index()
```

# 5 read csv modify df, rename columns
```python

df['mood'] = ['happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy',
                 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', 'happy', ]
df['mood'] = df.company.apply(lambda x: 'happy' if x == 'Uber' else 'unhappy')
df.columns = ['column 1', 'column 2', 'column 3',
              'column 4', 'column 5', 'column 6', ]
df = df.rename(columns={'id': 'ID'})
df = df.rename(str.upper, axis=1)
df['total_wage'] = df.apply(
    lambda x: x.hours_worked*x.hourly_wage, axis='columns')
df['total_wage'] = df['hourly_wage']*df['hours_worked']
```

# 6 df calculation, max(),groupby, nunique, unique,pivot table
```python
df['total_wage'] = df.apply(
    lambda x: x.hours_worked*x.hourly_wage, axis='columns')
df['total_wage'] = df['hourly_wage']*df['hours_worked']

max_wage = df.total_wage.max()
maxwag_cmp = df.groupby('company').total_wage.max()
maxwagcmp_idx = df.groupby('company').total_wage.max().reset_index()
company_num = df.company.nunique()
company_list = df.company.unique()
stafcmp = df.groupby('company').id.count().reset_index()
stafgencmp = df.groupby(['company', 'gender']).id.count().reset_index()
table = pd.pivot_table(stafgencmp, values='id',
                       columns='gender', index='company')

```

<++>
