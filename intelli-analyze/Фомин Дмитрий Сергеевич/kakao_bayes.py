
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

df_rating = df.where(df['Rating']>3.1).groupby('Company Location').size()
df_perc = dfper.where(dfper['Cocoa Percent']>73).groupby('Company Location').size()
dfBoth = dfper.where((dfper['Cocoa Percent']>73)&(dfper['Rating']>3.1)).groupby('Company Location').size()
df_rating_prob = df_rating / df1
df_perc_prob =df_perc / df1
dfBoth_prob= dfBoth / df1 
 

EU_AF = ['Amsterdam', 'Austria', 'Belgium','Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Ghana', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal','South Africa', 'Scotland', 'Spain', 'Sweden', 'Switzerland', 'U.K.', 'Wales']
 
pA = df_rating_prob.loc[EU_AF] 
pB = df_perc_prob.loc[EU_AF] 
pBA = dfBoth_prob.loc[EU_AF] 

print(bayes(pA,pB,pBA))
