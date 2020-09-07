import pandas as pd


visits = pd.read_csv('./vc_Case/visits.csv', parse_dates=[1])
checkouts = pd.read_csv('./vc_Case/checkouts.csv', parse_dates=[1])
v_c = pd.merge(visits, checkouts)
v_c['time'] = v_c.checkout_time - v_c.visit_time
print(v_c.head())
v_c.to_csv('vc.csv')
# print(visit)
# print(visits)
# print(checkouts)
