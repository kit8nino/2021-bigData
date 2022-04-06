import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

all_ref = data['REF'].dropna()
all_rating = data['Rating'].dropna()
all_percent = data["Cocoa Percent"].dropna()
df = pd.concat([all_ref, all_rating], axis=1)

f_ref = []
convert_perc = []

for i in all_ref:
    f_ref.append(str(i)[0])

df['fREF'] = f_ref
df = df.sort_values(by='fREF').groupby('fREF')

for i in all_percent:
    convert_perc.append(float(i.rstrip('%')))

convert_df_cocoa = pd.DataFrame(convert_perc, columns=["Cocoa Percent"])

df_cocoa = pd.concat([all_rating, convert_df_cocoa], axis=1).sort_values(
    by="Cocoa Percent").groupby('Cocoa Percent')

plt.figure(1)

plt.plot(df.mean()['Rating'], label='Усредненный график')
plt.axhline(df.mean()['Rating'].median(), linestyle=':',
            color='b', label='Медиана по средним')
plt.axhline(all_rating.median(), linestyle='-.',
            color='b', label='Медиана по всем')
plt.axhline(all_rating.mean(), linestyle='-.',
            color='r', label='Среднее по всем')

table_dt = {'По всем': [round(all_rating.var(), 2), round(all_rating.std(), 2)],
            'По средним': [round(df.mean()['Rating'].var(), 2), round(df.mean()['Rating'].std(), 2)]}

table_df = pd.DataFrame(data=table_dt, index=["Дисперсия", "СКО"])
plt.table(cellText=table_df.values,
          colWidths=[0.3, 0.3],
          rowLabels=table_df.index,
          colLabels=list(table_dt.keys()),
          rowColours=["lightgray"] * 2,
          colColours=["lightgray"] * 2,
          bbox=[0.2, -0.3, 0.6, 0.2],
          cellLoc='center')

plt.subplots_adjust(bottom=0.25)
plt.legend()

plt.figure(2, figsize=[13, 4.8])

plt.plot(df_cocoa.mean())
plt.plot(df_cocoa['Rating'].max(), color='lightgreen')
plt.plot(df_cocoa['Rating'].min(), color='r')
plt.plot(df_cocoa['Rating'].var(), color='black')

perc_xticks = list(df_cocoa['Cocoa Percent'].groups.keys())

plt.xticks(perc_xticks, [str(x).rstrip('0').rstrip('.')
                         for x in perc_xticks], rotation=70, size=9)

plt.legend(['Mean rating', 'Max', 'Min', 'Var'])
plt.subplots_adjust(right=0.98, left=0.02)
plt.show()
