import pandas as pd


amazon = pd.read_csv('amazon.csv', index_col=0)
tesla = pd.read_csv('tesla.csv', index_col=0)

amazon.columns = [col.lower() for col in amazon.columns]
amazon.columns = ['amzn_'+str(col) for col in amazon.columns]


tesla.columns = [col.lower() for col in tesla.columns]
tesla.columns = ['tsla_'+str(col) for col in tesla.columns]

print(amazon)
print()
print(tesla)