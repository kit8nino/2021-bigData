import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

print(data.head())

print(data.sort_values(by='Review Date').groupby("Review Date")[['Review Date', 'Rating']].mean())
rdate = data.sort_values(by='Review Date').groupby("Review Date")[['Review Date', 'Rating']].mean()
print(rdate)
print(rdate.Rating)
plt.plot(rdate['Review Date'], rdate['Rating'])
plt.axhline(data['Rating'].mean())
plt.show()

borig = data.sort_values(by='Broad Bean Origin').groupby("Broad Bean Origin")[['Broad Bean Origin', 'Rating']].mean()
print(borig)
print(borig.Rating)
plt.plot(borig['Rating'])
plt.axhline(data['Rating'].mean())
plt.show()
