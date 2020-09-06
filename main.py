import pandas as pd

df = pd.read_csv('employee.csv')

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

# print(max_wage)
# print(company_list)
# print(company_num)
# print(maxwag_cmp)
# print(maxwagcmp_idx)
# print(stafcmp)

print(stafgencmp)
table = pd.pivot_table(stafgencmp, values='id',
                       columns='gender', index='company').reset_index()
print(table)
print(df)
