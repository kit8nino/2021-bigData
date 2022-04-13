import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)
rating = data['Rating']
