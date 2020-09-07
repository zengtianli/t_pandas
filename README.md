# Introduction to Panda
## create, load, select data with pandas
### create
```python
df = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'product_name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'color': ['blue', 'green', 'red', 'black'],
})
df = pd.DataFrame([
    [1, 't-shirt', 'blue'],
    [2, 't-shirt', 'green'],
    [3, 'skirt', 'red'],
    [4, 'skirt', 'black'],
],
    columns=['product_id', 'product_name', 'color'])

```
### load/save csv, select columns
```python
df.read_csv('employee.csv')
df.read_csv('outemployee.csv')
dfpro_id = df.product_id
dfpro_pid = df[['product_id', 'product_name']]
```

### select rows, multiple rows
```python
orders.iloc[1]
orders.iloc[1,1]
orders.iloc[1:3]
print(df.head())
print(df.info())
print(type(df))
```

### select rows with logic

```python
hz = df[df.city_name == 'Hangzhou']
hznj = df[(df.city_name == 'Hangzhou') | (df.city_name == 'Nanjing')]
hznj = df[df.city_name.isin(['Hangzhou', 'Nanjing'])]
hznj.reset_index(inplace=True, drop=True)
hznj.reset_index(inplace=True)
hznj1 = hznj.reset_index()
```
### setting indices
```python
df.iloc[[1,3]]
df.reset_index()
df.reset_index(inplace=True,drop=True)

```
## modify DataFrame
### add columns

```python
df['new_col0'] = 1
df['new_col1'] = [i for i in range(20)]
df['after_tx'] = df.salary*0.99
```
### apply lambda to column and columns

```python
df['mood'] = df.company.apply(lambda x: 'happy' if x == 'Uber' else 'unhappy')
df['total_wage'] = df.apply(
    lambda x: x.hours_worked*x.hourly_wage, axis='columns')
df['total_wage'] = df.apply(
    lambda x: x.hours_worked*x.hourly_wage, axis='columns')
```
### Rename Columns
```python
df.columns = ['Id', 'C', 'S']
df.rename(columns={'id': 'ID'}, inplace=True)
df.rename(str.upper, axis='columns', inplace=True)
```

# Aggregates in Pandas

## calculating, max() reset_index() count() nunique() unique()
```python
df.read_csv('employee.csv')
max_wage = df.total_wage.max()
maxwag_cmp = df.groupby('company').total_wage.max()
maxwagcmp_idx = df.groupby('company').total_wage.max().reset_index()
company_num = df.company.nunique()
company_list = df.company.unique()
stafcmp = df.groupby('company').id.count().reset_index()
```

## pivot_table
```python 
stafgencmp = df.groupby(['company', 'gender']).id.count().reset_index()
table = pd.pivot_table(stafgencmp, values='id',
                       columns='gender', index='company')
```

# Multiple Table in Pandas

## inner merge
```python
all_data = sales.merge(targets).merge(mw_sales)
sales_targets = pd.merge(sales, targets)
re_gt_tag = sales_targets[sales_targets.revenue > sales_targets.target]
re_gt_tag_wm = all_data[(all_data.revenue > all_data.target)
                        & (all_data.women > all_data.men)]

```

## merge on Specific columns mismatch
```python

orders = pd.read_csv('./spe_merge/orders.csv')
products = pd.read_csv('./spe_merge/products.csv')
ord_prd_mg = pd.merge(orders, products)
ord_prd_smg = pd.merge(orders, products.rename(columns={'id': 'product_id'}))
```

## merge outer
```python

store_a = pd.read_csv('./out_merge/store_a.csv')
store_b = pd.read_csv('./out_merge/store_b.csv')
ab_outer = pd.merge(store_a, store_b, how='outer')
```

## merge left
```python

ab_left = pd.merge(store_a, store_b, how='left')
ab_right = pd.merge(store_a, store_b, how='right')
ba_left = pd.merge(store_b, store_a, how='left')
```

## concatenate df
```python

bakery = pd.read_csv('./cat/bakery.csv')
ice_cream = pd.read_csv('./cat/ice_cream.csv')
menu = pd.concat([bakery, ice_cream])
```

