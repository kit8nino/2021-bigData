import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

all_ref = data['REF'].dropna()
all_rating = data['Rating'].dropna()
df = pd.concat([all_ref, all_rating], axis=1)

f_ref = []

for i in all_ref:
	f_ref.append(str(i)[0])

df['fREF'] = f_ref
df = df.sort_values(by='fREF').groupby('fREF')

print(all_rating.median())

plt.plot(df.mean()['Rating'])

plt.show()