import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

rating = data['Rating']
ref = data[['REF', 'Rating']]

def lowNums(x):
  while len(str(x['REF'].max())) >= 2:
        x.loc[x['REF'] > 9, 'REF'] //= 10
    return 1

  
lowNums(ref)
ref = ref.groupby(by="REF")[['REF', 'Rating']]
