import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']
ref = data[['REF', 'Rating']]
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
cacao = data[['Cocoa Percent', 'Rating']].sort_values(by="Cocoa Percent").groupby('Cocoa Percent')
print(data.head())
while len(str(ref['REF'].max())) >= 2:
        ref.loc[ref['REF'] > 9, 'REF'] //= 10
        
ref = ref.groupby(by="REF")[['REF', 'Rating']]
plt.figure(1, figsize=[15, 8])
plt.subplot(2,2,1)
plt.plot(ref.mean()['Rating'], label='graph')
plt.axhline(rating.mean(), color='r', label='Average')
plt.xlabel("REF")
plt.ylabel("Rating")
plt.legend()

plt.subplot(2,2,2)
plt.plot(ref.var()['Rating'], label='graph')
plt.axhline(rating.var(), color='r', label='Average')
plt.xlabel("REF")
plt.ylabel("Rating")
plt.legend()

plt.subplot(2,2,3)
plt.plot(ref.std()['Rating'], label='graph')
plt.axhline(rating.std(), color='r', label='Average')
plt.xlabel("REF")
plt.ylabel("Rating")
plt.legend()

plt.legend()
plt.show()

plt.figure(2, figsize=[10, 5])
plt.plot(cacao['Rating'].max(), color='b')
plt.plot(cacao.mean(), color='g')
plt.plot(cacao['Rating'].min(), color='r')
plt.plot(cacao['Rating'].var(), color='orange')
plt.legend(['Max', 'Average', 'Min', 'Dispersion'])
plt.show()
