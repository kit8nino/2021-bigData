import pandas as pd
import matplotlib.pyplot as plt

mainDF = pd.read_csv('./flavors_of_cacao.csv', header=0)
mainDF['Cocoa Percent'] = mainDF['Cocoa Percent'].replace('%', '', regex=True).astype('float64')

tempDF1 = mainDF.query('Rating > 3.1')
tempDF2 = mainDF.groupby('Company Location')
tempDF1 = tempDF1.groupby('Company Location')
tempDF = (tempDF1['Rating'].count() / tempDF2['Rating'].count()).dropna()

print('[1] Вероятность получения оценки выше 3.1')
print(tempDF)


bothAmericas = ['Bolivia', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'U.S.A.']




tempDF = mainDF.query('`Review Date` > 2014')
medianValue = mainDF.query('`Review Date` > 2010')['Rating'].median()
tempDF = tempDF.query(f'Rating > {medianValue}')['Rating'].count() / tempDF['Rating'].count()
print('[3] Прогноз вероятности, что обзоры после 2014 года будут иметь оценку'
      ' выше медианной по всему периоду 2010 года')
print(tempDF)