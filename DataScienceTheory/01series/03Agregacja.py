import pandas as pd
import numpy as np


# %% generowanie danych

np.random.seed(0)

s = pd.Series(np.random.randn(20))

# %% Agregacja


minimum = s.aggregate(min)
maximum = s.aggregate(max)

suma = s.aggregate(sum)

mean = s.aggregate(np.mean)
std = s.aggregate(np.std)

# %%
stats = s.aggregate(['min','max','sum','mean']) #zrobi to co wczeniej ale nie w oddzielnych zmiennych tylko jako statystyki opisowe, tzn index=nazwa_funkcji i wartosc, zwraca dataSeries

stats_np = s.aggregate([np.mean, np.std, np.median])
#zapisy równoważne wyżej i niżej
stats_my = s.aggregate(['mean','std','median'])