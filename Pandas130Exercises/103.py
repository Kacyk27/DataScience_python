import pandas as pd


pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)

df = pd.read_json('market.json')
print(df)