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

# print(df.head())

plt.plot(df.mean()['Rating'],label='Усредненный график')
# plt.plot(df['Rating'],'ro',label='Общий график')

plt.axhline(df.mean()['Rating'].var(),linestyle=':',color='k',label='Дисперсия по ср.')
plt.axhline(all_rating.var(),linestyle='-.',color='k',label='Дисперсия по общим')

plt.axhline(df.mean()['Rating'].median(),linestyle=':',color='b',label='Медиана по ср.')
plt.axhline(all_rating.median(),linestyle='-.',color='b',label='Медиана по общим')

plt.axhline(df.mean()['Rating'].std(),linestyle=':',color='g',label='СКО по ср.')
plt.axhline(all_rating.std(),linestyle='-.',color='g',label='СКО по общим')

plt.legend()
plt.show()