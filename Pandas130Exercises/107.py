import pandas as pd


pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
df = pd.read_json('market.json')
df['Zmiana %'] = df['Zmiana %'].apply(lambda item: float(item[1:-2]))

print(df.iloc[df['Zmiana %'].argmax()])
print()
print(df.iloc[df['Zmiana %'].argmin()])