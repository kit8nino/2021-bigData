import numpy as np
import pandas as pd

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1, df2], axis=1)
data.columns = [x for x in range(7)]

print(data.head())

#data.to_csv('Konnov' , sep='\t')

for i in range(100):
    data.at[np.random.randint(9000), 0] /= 2
    data.at[np.random.randint(9000), 1] = None
    data.at[np.random.randint(9000), 5] = -9999999999
    data.at[np.random.randint(9000), 6] = None

df = pd.read_csv('Konnov', sep='\t', header=0, index_col=0)
df.columns = [x for x in range(7)]



medium_value = sum(df[4]+df[5]+df[6])/(len(df[4])+len(df[5])+len(df[6]))

print(medium_value)
min_int_value = int(sum([df[0].mean(), df[1].mean(), df[2].mean(), df[3].mean()])) % 100
print(min_int_value)

from math import factorial
print(factorial(min_int_value))

def fact(x):
    if x<2:
        return 1
    else:
        return x*fact(x-1)
print(fact(min_int_value))