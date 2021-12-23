import pandas as pd


pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)

amazon = pd.read_csv('amazon.csv', index_col=0)
tesla = pd.read_csv('tesla.csv', index_col=0)
amazon.columns = ['amzn_' + col.lower() for col in amazon.columns]
tesla.columns = ['tsla_' + col.lower() for col in tesla.columns]

result = pd.concat([amazon,tesla], axis=1)
print(result)