import pandas as pd


#%% lokalnie

df = pd.read_html('./data/small.html',header=0,index_col=0)[0] #0 na końcu wycina tą tabelę z utworzonej listy tabel

#%% z neta

df_ = pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20')[0]

#%%

#df______ = pd.read_html('https://stooq.pl/t/?i=516')
#BRAK TABEL NA STRONIE, zmienili kod źródłowy w od 2019.
#%%
df__ = pd.read_html('https://finance.yahoo.com/cryptocurrencies')
# również nie wyszukuje tabel.





