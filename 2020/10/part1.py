import itertools
import pandas as pd

with open('input.txt') as f:
    data = f.read().split("\n")

data = [int(d) for d in data]
data.sort()
print(data)

difs = [data[0]]
print(len(data))

for i in range(1, len(data)):
    difs.append(data[i] - data[i-1])

difs.append(3)

difs = pd.Series(difs)
print(difs)
print(difs.value_counts())

print(66*32)

