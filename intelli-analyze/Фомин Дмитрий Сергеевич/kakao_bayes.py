import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


data = pd.read_csv('flavors_of_cacao.csv',header=0)

def bayes(pA, pB, pBA):
    return pBA*pA/pB


loc = data['Company Location'].dropna()
rat = data['Rating'].dropna()
per = data['Cocoa Percent'].dropna().apply(lambda x: float(x.strip('%')))

df = pd.concat([loc, rat], axis=1)
df1 = pd.concat([loc, rat], axis=1).groupby('Company Location').size()
dfper = pd.concat([loc, rat, per], axis=1)
dfper1 = pd.concat([loc, rat, per], axis=1).groupby('Company Location').size()

df2 = df.where(df['Rating']>3.1).groupby('Company Location').size()
notdf22 = dfper.where((dfper['Rating']<3.1) & (dfper['Cocoa Percent']>73)).groupby('Company Location').size()
df22 = dfper.where((dfper['Rating']>3.1) & (dfper['Cocoa Percent']>73)).groupby('Company Location').size()
df3 = df2 / df1
df33 = df22/ dfper1
notdf33= notdf22 / dfper1 
print(df3) 

EU_AF = ['Amsterdam', 'Austria', 'Belgium', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Ghana', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal', 'Scotland', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'U.K.', 'Wales']

df4 = df3.loc[EU_AF] #pa
df5 = df33.loc[EU_AF] #pba
df6 = notdf33.loc[EU_AF] #pbna
pB = df5*df4 + df6*(1-df4)

print(bayes(df4,pB,df5))
