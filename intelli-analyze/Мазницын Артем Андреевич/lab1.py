import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def lowNums(x):
  while len(str(x['REF'].max())) >= 2:
        x.loc[x['REF'] > 9, 'REF'] //= 10
    return 1

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']
ref = data[['REF', 'Rating']]
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)
cocao = data[['Cocoa Percent', 'Rating']].sort_values(by="Cocoa Percent").groupby('Cocoa Percent')


lowNums(ref)
ref = ref.groupby(by="REF")[['REF', 'Rating']]

plt.figure(1)

plt.plot(ref.mean()['Rating'], label='Усредненный график')
plt.axhline(rating.mean(), linestyle='--',color='r', label='Общее среднее')
tab = {'Медиана': [round(rating.median(), 3), round(ref.mean()['Rating'].median(), 3)],
            'Дисперсия': [ round(rating.var(), 3), round(ref.mean()['Rating'].var(), 3)],
       'СКО': [round(rating.std(), 3), round(ref.mean()['Rating'].std(), 3)]
       }
tab_df = pd.DataFrame(data=tab, index=["По всем", "По средним"])
plt.table(cellText=tab_df.values,
          colWidths=[0.2, 0.2, 0.2],
          rowLabels=tab_df.index,
          colLabels=list(tab.keys()),
          rowColours=["lightgray"] * 3,
          colColours=["lightgray"] * 3,
          bbox=[0.3, -0.4, 0.6, 0.3],
          cellLoc='center')

plt.subplots_adjust(bottom=0.3)
plt.legend()

plt.show()


plt.figure(2, figsize=[12, 5])

plt.plot(cocoa.mean())
plt.plot(cocoa['Rating'].max(), color='b')
plt.plot(cocoa['Rating'].min(), color='r')
plt.plot(cocoa['Rating'].var(), color='black')

cols = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique()
cols = cols.astype(str)
cols = [i.replace('.0', '') for i in cols]

plt.xticks(col, rotation=90, size=9)

plt.legend(['Средний рейтинг', 'Максимальный', 'Минимальный', 'Дисперсия'])
plt.show()
