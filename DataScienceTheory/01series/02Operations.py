import pandas as pd
import numpy as np


#generowanie danych

np.random.seed(0)

A = np.random.randint(0,10,10)

series = pd.Series(A, name='los')

# %% atrybuty

series.dtype #mówi o rodzaju zmiennych w obiekcie

series.iloc[-1] #wycinanie elementów
series.iloc[1]
series.index #zwraca ile indeksów
series.name #zwraca nazwę
series.shape #zwraca kształt czyli rozmiar

array_A = series.values


# %% 

N = np.random.randn(10) #randn - rozkład normalny, w nawiasie ilosc liczb
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)


# %% Metody podstawowe

series_N.abs() #zwraca wartosci bezwzgledne
series_N.add(series_M)
series_N.sub(series_M)
series_N.div(series_M)
series_N/series_M #działa tak jak wyżej. są metody, ale są też proste operatory.

series.drop_duplicates() #usuwa zdublowane wartosci

series[4] = np.nan
series.dropna()

series.idxmax()
series.idxmin() #indeksy max i min wartoci

series.count() #zlicza wartosci i pomija nan

series_N.cumsum() #idzie od góry do dołu i sumuje kolejne wartosci

series_N.cummin() #zwraca po kolej najmniejszą napotkaną wartosc

series_N.cummax() #przeciwieństwo cummin

series.value_counts() #zlicza ile razy wystąpił dany element i sortuje według częstosci wystapienia

series.sum() #sumuje wartosci, pomija nan

series.std() #odchylenie standardowe

series.describe() #percentyle, ilosc, srednia, odchylenie, minimalna, maksymalna, mediana (2 percentyl, tzn 50%.)

# %% Tworzenie histogramu

hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='royalblue')

# %% top n
top_3 = series_N.nlargest(3) #3 najwyższe wyniki zwraca
top_3

# bottom n
bottom_4 = series_N.nsmallest(4)

kwartyl_1 = series_N.quantile(0.25)
kwartyl_2 = series_N.quantile(0.5) #mediana
kwartyl_3 = series_N.quantile(0.75)

series_N.round(3)

# %%

shift_1 = series.shift(1) # na początku daje nan, przesuwa wszystko o jeden dalej, ostatni index znika

shift_2_replace_0 = series.shift(2).fillna(0) #uzupełnia wartoci NaN daną wartoscia

# %%

sorted_series = series.sort_values() #od najniższej do najwyższej
sorted_series = series.sort_values(ascending=False) #od najwyższej do najniższej



















