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
plt.figure(1)
plt.plot(df.mean()['Rating'],label='Усредненный график')
# plt.plot(df['Rating'],'ro',label='Общий график')

# plt.axhline(df.mean()['Rating'].var(),linestyle=':',color='k',label='Дисперсия по ср.')
# plt.axhline(all_rating.var(),linestyle='-.',color='k',label='Дисперсия по общим')

plt.axhline(df.mean()['Rating'].median(),linestyle=':',color='b',label='Медиана по средним')
plt.axhline(all_rating.median(),linestyle='-.',color='b',label='Медиана по общим')

plt.axhline(all_rating.mean(),linestyle='-.',color='r',label='Общее среднее')

# plt.axhline(df.mean()['Rating'].std(),linestyle=':',color='g',label='СКО по ср.')
# plt.axhline(all_rating.std(),linestyle='-.',color='g',label='СКО по общим')

columns = ("По общим","По средним")
rows = ("Дисперсия","СКО")
n_rows = 10
cell_text = [1,1]

dt_raw = {'По общим'  :[round(all_rating.var(),2),round(all_rating.std(),2)],
		  'По средним':[round(df.mean()['Rating'].var(),2),round(df.mean()['Rating'].std(),2)]}

dt_DF = pd.DataFrame(data=dt_raw,index = ["Дисперсия","СКО"])
plt.table(cellText=dt_DF.values,
		  colWidths = [0.3, 0.3],
          rowLabels=rows,
          colLabels=columns,
          rowColours=["lightgray"]*2,
          colColours=["lightgray"]*2,
          # loc='bottom',
          bbox = [0.2,-0.3,0.6,0.2],
          cellLoc='center')

plt.subplots_adjust(left=0.2, bottom=0.25)

# plt.figure(2)


plt.legend()
plt.show()