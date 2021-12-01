import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('battles.csv', header=0)

attacker = data.groupby(['attacker_king', 'year'], dropna=True)[['year']]
attacker.agg('count').to_csv('attacker', sep=',')

defender = data.groupby(['defender_king', 'year'], dropna=True)[['year']]
defender.agg('count').to_csv('defender', sep=',')

df1 = pd.read_csv('attacker', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
df2 = pd.read_csv('defender', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)

df4 = df3.groupby(['king', 'year'], dropna=True)[['count']]
df4.agg('sum').to_csv('result', sep='\t')
df4 = pd.read_csv('result', header=0, sep='\t', na_filter=True, names=['king', 'year', 'count'])
print(df4)


x = df4['year']
y = df4['king']
c=df4['count']
fig, ax = plt.subplots()
plt.scatter(x, y,c*12) 
plt.xlabel('Year')

for x1, y1, s1 in zip(x, y, c):
    label = s1
    plt.annotate(s1,
                (x1, y1),
                 textcoords="offset points",
                 xytext=(6, -4),
                 ha='left',fontsize=14)

ax.set(xlim=(297, 301), xticks=np.arange(298, 301))
plt.show()
