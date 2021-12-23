import pandas as pd


pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
df = pd.read_json('market.json')
df['Kraj'] = df['Profil'].str.split(n=1, expand=True)[1].apply(lambda item: item[1:-1])

x = df['Kraj'].value_counts()
x = x.where(x>1).dropna()
print(sorted(list(x.index)))

