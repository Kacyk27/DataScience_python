import pandas as pd


pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
df = pd.read_json('market.json')

df['Kraj'] = df['Profil'].str.replace("(","").str.replace(")","").str.split(" ",1)
df['Kraj']= df['Kraj'].apply(lambda x: x[1])
print(df)