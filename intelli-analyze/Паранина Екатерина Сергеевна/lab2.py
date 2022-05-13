import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)


all_cl = data['Company Location'].dropna()
all_rating = data['Rating'].dropna()
all_percent = data['Cocoa Percent'].dropna().apply(
    lambda x: float(x.strip('%')))

dt = pd.concat([all_cl, all_rating], axis=1)
dtt = pd.concat([all_cl, all_rating,all_percent], axis=1)


dt1 = pd.concat([all_cl, all_rating], axis=1).groupby('Company Location').size()
dt11 = pd.concat([all_cl, all_rating,all_percent], axis=1).groupby('Company Location').size()


dt2=dt.where(dt['Rating']>3.1).dropna()
dt22=dtt.where((dtt['Rating']>3.1) & (dtt['Cocoa Percent']>73)).dropna()
dt222=dtt.where((dtt['Rating']<=3.1) & (dtt['Cocoa Percent']>73)).dropna()
dt2=dt2.groupby('Company Location').size()
dt22=dt22.groupby('Company Location').size()
dt222=dt222.groupby('Company Location').size()

dt3=dt2.div(dt1)
dt33=dt22.div(dt11)
dt333=dt222.div(dt11)

print('априорные вероятности для каждой страны происхождения получения оценки выше 3.1')
print(dt3)

print('---------')
#print(dt1)
#print(dt2)

def bayes(pA, pB, pBA):
    return pBA*pA/pB


south_countries=['Argentina','Australia','Bolivia','Brazil','Chile','Colombia','Ecuador','Fiji','Madagascar','New Zealand','Peru','South Africa']
a=dt3.loc[south_countries]
ba=dt33.loc[south_countries]
bna=dt333.loc[south_countries]
b = ba*a + bna*(1-a)

print('вероятность того, что новый сорт какао с содержанием выше 73% будет имет оценку выше 3.1 для стран южного полушария:')
print(bayes(a, b, ba))




