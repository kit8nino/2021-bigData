import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
north = ['Amsterdam', 'Belgium', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'France', 'Israel', 'Italy',
                     'Lithuania', 'Sao Tome', 'Scotland', 'Switzerland', 'U.K.', 'U.S.A.']

datR = getData(data, 'Rating > 3.1').dropna()
plt.subplots(figsize=(14, 9))
ax = sns.barplot(y=datR.index, x=datR.array, palette='deep')
ax.set_title('Вероятность получения оценки выше 3.1')
ax.set_yticklabels(labels=datR.index, rotation=0)
plt.show()
