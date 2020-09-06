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

# 7 operation in multiple df
## 7.1 merge inner merge
```python
all_data = sales.merge(targets).merge(mw_sales)
sales_targets = pd.merge(sales, targets)
re_gt_tag = sales_targets[sales_targets.revenue > sales_targets.target]
re_gt_tag_wm = all_data[(all_data.revenue > all_data.target)
                        & (all_data.women > all_data.men)]

```

## 7.2 merge on specific columns

```python
orders = pd.read_csv('./spe_merge/orders.csv')
products = pd.read_csv('./spe_merge/products.csv')
ord_prd_mg = pd.merge(orders, products)
ord_prd_smg = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

```

<++>
