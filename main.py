import pandas as pd

orders = pd.read_csv('./spe_merge/orders.csv')
products = pd.read_csv('./spe_merge/products.csv')
ord_prd_mg = pd.merge(orders, products)
ord_prd_smg = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

print(orders)
print(products)

print(ord_prd_mg)
print(ord_prd_smg)
