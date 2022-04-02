import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

all_ref = data['REF'].dropna()
all_rating = data['Rating'].dropna()
all_percent = data["Cocoa Percent"].dropna()
df = pd.concat([all_ref, all_rating], axis=1)

f_ref = []
conv_perc = []
conv_perc_gb = []

for i in all_ref:
	f_ref.append(str(i)[0])

df['fREF'] = f_ref
df = df.sort_values(by='fREF').groupby('fREF')

for i in all_percent:
	conv_perc.append(float(i[:len(i)-1]))

for i in all_percent:
	conv_perc_gb.append(round(float(i[:len(i)-1])/10)*10)

convert_df_cocoa = pd.DataFrame(conv_perc,columns=["Cocoa Percent"])
df_cocoa = pd.concat([all_rating,convert_df_cocoa],axis = 1).sort_values(by="Cocoa Percent")

convert_df_cocoa_gb = pd.DataFrame(conv_perc_gb,columns=['gb_perc'])
df_cocoa_gb = pd.concat([all_rating,convert_df_cocoa_gb],axis = 1).sort_values(by = 'gb_perc').groupby('gb_perc')

plt.figure(1)

plt.plot(df.mean()['Rating'],label='Усредненный график')
plt.axhline(df.mean()['Rating'].median(),linestyle=':',color='b',label='Медиана по средним')
plt.axhline(all_rating.median(),linestyle='-.',color='b',label='Медиана по всем')
plt.axhline(all_rating.mean(),linestyle='-.',color='r',label='Среднее по всем')

columns = ("По всем","По средним")
rows = ("Дисперсия","СКО")
n_rows = 10
cell_text = [1,1]

dt_raw = {'По всем'  :[round(all_rating.var(),2),round(all_rating.std(),2)],
		  'По средним':[round(df.mean()['Rating'].var(),2),round(df.mean()['Rating'].std(),2)]}

dt_DF = pd.DataFrame(data=dt_raw,index = ["Дисперсия","СКО"])
plt.table(cellText=dt_DF.values,
		  colWidths = [0.3, 0.3],
          rowLabels=rows,
          colLabels=columns,
          rowColours=["lightgray"]*2,
          colColours=["lightgray"]*2,
          bbox = [0.2,-0.3,0.6,0.2],
          cellLoc='center')

plt.subplots_adjust(left=0.2, bottom=0.25)
plt.legend()

plt.figure(2)
shift=0.05

plt.plot(df_cocoa['Cocoa Percent'],df_cocoa['Rating'])
for i in df_cocoa_gb:
	print(i[1])
	plt.axhline(i[1]['Rating'].max(),linestyle='-',color='lightgreen',label='max',xmin=shift-0.04,xmax=shift+0.04)
	plt.axhline(i[1]['Rating'].min(),linestyle='-',color='r',label='min',xmin=shift-0.04,xmax=shift+0.04)
	plt.axhline(i[1]['Rating'].var(),linestyle='-.',color='black',label='var',xmin=shift-0.04,xmax=shift+0.04)
	shift+=0.15

plt.legend(['Rating','Max','Min','Var'])
plt.show()