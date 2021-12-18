import pandas as pd
import numpy as np


url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
#%% exploring dataset
retail.info()
cols=[col for col in retail.columns]
retail.head()
retail.tail()

#%%preprocessing
#drop rows with null
retail = retail[retail['CustomerID'].notnull()]

#convert type to string
retail['CustomerID'] = retail['CustomerID'].apply(lambda x: str(int(x)))
# exclude Quantity less than zero
retail = retail[retail['Quantity'] > 0]


#%%
"""
SELECT *
FROM retail
"""
query = retail

#%%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retail;
"""
query = retail[['Quantity','UnitPrice','CustomerID']]

#%%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retial
LIMIT 10;
"""
query = retail[['Quantity','UnitPrice','CustomerID']][:10]
query_ = retail[['Quantity','UnitPrice','CustomerID']].head(10) #równoważne

#%%
"""
SELECT *
FROM retial
WHERE CustomerID='17850';
"""
query = retail[retail['CustomerID'] == '17850'] #sposób 1

query_ = retail.query("CustomerID == '17850'") #sposób 2



#%% AND OR

#AND
"""
SELECT *
FROM retial
WHERE CustomerID='17850' and UnitPrice > 5;
"""

query = retail[(retail['CustomerID'] == '17850') & (retail['UnitPrice'] > 5)]

query_ = retail.query("CustomerID == '17850' and UnitPrice > 5")

#%% OR

"""
SELECT *
FROM retial
WHERE CustomerID='17850' or Country='France';
"""

query = retail[(retail['CustomerID'] == '17850') | (retail['Country'] == 'France')]

query_ = retail.query("CustomerID == '17850' or Country == 'France'")
#%% ISNULL
"""
SELECT *
FROM retail
WHERE InvoiceNo is null;
"""
query = retail[retail['InvoiceNo'].isnull()]
query = retail[retail['StockCode'].isnull()]

#%% Is Not Null
"""
SELECT *
FROM retail
WHERE InvoiceNo is not null;
"""
query = retail[retail['InvoiceNo'].notnull()]

#%% GROUP BY
"""
SELECT CustomerID, count(*)
FROM retial
GROUP BY CustomerID;
"""
cust_id = retail.groupby('CustomerID').size()
country = retail.groupby('Country').size()

#%% compute new cols Revenue

retail['Revenue'] = retail['Quantity'] * retail['UnitPrice']

#%% groupy by
"""
SELECT CustomerID, avg(Revenue), count(*)
FROM retial
GROUP BY CustomerID;
"""

result = retail.groupby('CustomerID').agg({'Revenue':np.mean, 'CustomerID':np.size}).rename(columns={"Revenue":'Average_Revenue',
                                                                                                     'CustomerID':'Count_Customer'})

#%% making InvoiceDateDay column

retail['InvoiceDay'] = retail['InvoiceDate'].dt.day

query = retail.groupby('InvoiceDay').agg({'Revenue':sum})
query.plot(kind='bar', color='black', alpha=0.5)

#%% grouping by InvoiceDateDay 9 
mask= (retail['InvoiceDate'] > '2010-12-09')  & (retail['InvoiceDate'] < '2010-12-10')
day9 = retail[mask]
day9['Hour'] = day9['InvoiceDate'].dt.hour

query = day9.groupby('Hour').agg({"Revenue":np.sum})
query.plot(kind='bar',color='blue',alpha=0.5)


#%% top n rows
"""
SELECT * FROM retail
ORDER BY Quantity DESC
LIMIT 5;
"""

query = retail.nlargest(5, columns='Quantity')

#%% bottom n rows
"""
SELECT * FROM retail
ORDER BY Quantity DESC
LIMIT 10;
"""

query = retail.nsmallest(10, columns=('Quantity'))
query = retail.sort_values('Quantity', ascending=False)

