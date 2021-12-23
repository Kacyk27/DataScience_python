import pandas as pd


pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)

amazon = pd.read_csv('amazon.csv', index_col=0)
tesla = pd.read_csv('tesla.csv', index_col=0)
amazon.columns = ['amzn_' + col.lower() for col in amazon.columns]
tesla.columns = ['tsla_' + col.lower() for col in tesla.columns]
result = pd.concat([amazon, tesla], axis=1)
quotations = result[['amzn_open', 'amzn_close', 'tsla_open', 'tsla_close']].copy()

quotations['amzn_change'] = (quotations['amzn_close'] / quotations['amzn_open'] - 1) *100

quotations['tsla_change'] = (quotations['tsla_close'] / quotations['tsla_open'] - 1) *100

print(quotations)