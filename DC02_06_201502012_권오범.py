import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names=['word','bin'])

count = 1
minimum = list()
row = df.shape[0]
for i in range[0, row-1]:
    for j in range[i+1, row]:
        hd = hamming(df.iloc[i,1], df.iloc[j,1])
        print(count, "(", df.iloc[i,0], df.iloc[j,0],") hamming_distance", hd)
        minimum.append(hd)
        x = min(minimum)
        count += 1

print("min hamming distance", x)
