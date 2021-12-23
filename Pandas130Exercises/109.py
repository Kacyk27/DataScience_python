import pandas as pd

amazon = pd.read_csv('amazon.csv', index_col=('Date'))

tesla = pd.read_csv('tesla.csv', index_col=('Date'))

print(amazon)
print()
print(tesla)