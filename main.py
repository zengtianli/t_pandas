import pandas as pd
df = pd.read_csv('employee.csv')
df_lyft = df[df.company == 'Lyft']
# print(df_lyft)
# df_lyftdidi = df[(df.company == 'Lyft') | (df.company == 'Didi')]
# print(df_lyftdidi)
df_isin = df[df.company.isin(['Lyft', 'Didi'])]
df_isin_reidx = df_isin.reset_index()
# print(df_isin_reidx)
# print(df_isin)
# df_isin_reidx = df_isin.reset_index(drop=True, inplace=True)
# print(df_isin_reidx)
# print(df_isin)

df['new_col0'] = 1
df['new_col1'] = [i for i in range(20)]
print(df)
