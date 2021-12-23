import pandas as pd


pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df = pd.DataFrame(data)
for col in ['size', 'color', 'gender', 'bought']:
    df[col] = df[col].astype('category')

df['weight'] = df['weight'].astype('float')

print(pd.get_dummies(df))