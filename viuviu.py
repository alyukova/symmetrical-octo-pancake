import math
import numpy as np
import pandas as pd
import statistics
import scipy.stats as stats
data = pd.read_csv('lawnmower_var_144846.csv',
                   delimiter=',',
                   decimal='.')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
me3035 = []
avg3640 = []
me4145 = []
for i in range(200):
    if 30 <= data['WIDTH'][i] <= 35:
        me3035.append(data['WIDTH'][i])
    elif 36 <= data['WIDTH'][i] <= 40:
        avg3640.append(data['WIDTH'][i])
    elif 41 <= data['WIDTH'][i] <= 45:
        me4145.append(data['WIDTH'][i])
for i in range(200):
    if math.isnan(data["WIDTH"][i]):
        if 'Узк' in data['DESCRIPTION'][i]:
            data['WIDTH'][i] = statistics.median(me3035)
        elif 'Средн' in data['DESCRIPTION'][i]:
            data['WIDTH'][i] = round(statistics.mean(avg3640))
        elif 'Широкая' in data['DESCRIPTION'][i]:
            data['WIDTH'][i] = statistics.median(me4145)
avgrass = statistics.mean(data['WIDTH'])
print(statistics.median(me3035))
print(round(statistics.mean(avg3640)))
print(statistics.median(me4145))
print(avgrass)
# print(data[['DESCRIPTION', 'GRASS']])
# data['GRASS'].quantile(0.25, 0.75)
Q1 = data['PRICE'].quantile(q=.25)
Q2 = data['PRICE'].quantile(q=.75)
IQR = Q2 - Q1
# data.plt.boxplot(column=['GRASS']
# print(IQR, Q1, Q2)
maxp = Q2 + 3*IQR
minp = Q1 - 3*IQR
for i in range(200):
    if data['PRICE'][i] > maxp or data['PRICE'][i] < minp:
        data['PRICE'][i] = np.nan
data = data.dropna()
data = data.reset_index()
# print(data['PRICE'])
avgprice = statistics.mean(data['PRICE'])
# print(avgprice)
data['WIDTH'] = (data['WIDTH'] - data['WIDTH'].min())/(data['WIDTH'].max() - data['WIDTH'].min())
data['PRICE'] = (data['PRICE'] - data['PRICE'].min())/(data['PRICE'].max() - data['PRICE'].min())
data['POWER'] = (data['POWER'] - data['POWER'].min())/(data['POWER'].max() - data['POWER'].min())
data['GRASS'] = (data['GRASS'] - data['GRASS'].min())/(data['GRASS'].max() - data['GRASS'].min())
data['AREA'] = (data['AREA'] - data['AREA'].min())/(data['AREA'].max() - data['AREA'].min())
# Нормированная ширина скашиваемой полосы с коэффициентом 3
# Стоимость как слагаемое вида (1 - нормированная стоимость) с коэффициентом 1
# Нормированную мощность с коэффициентом 1
# Нормированный объём травосборника с коэффициентом 2
# Нормированную площадь скашиваемой поверхности с коэффициентом 8
# print(data.loc[data['NAME'] == 'Bear BCR815'])
# data = 1 - np.exp(1-data/data.min())
# Bear BCR815:   119    147      Bear BCR815  0.071429  0.097561  0.291667    0.5  1.000
data['SUM'] = 3*data['WIDTH'] + (1 - data['PRICE']) + data['POWER'] + 2*data['GRASS'] + 8*data['AREA']
data = data.sort_values(by = ['SUM'])
print(data)
# print(data[['NAME', 'SUM']])
    # if 30 <= data['GRASS'][i] <= 35:data.loc['GRASS'[i]< min,i] = np.nan
    # data.loc['GRASS'[i] > max,i] = np.nan
# data_clean = data[~((data < (Q1-1.5*IQR)) | (data > (Q2+1.5*IQR))).any(axis=1)]
# print(data_clean)
# data = (data['GRASS'] < Q1-1.5*IQR) | (data['GRASS'] > Q2+1.5*IQR)
# print(data.shape())
# avg = 0 191 158 17
# Q1, Q2 = data['GRASS'].quantile([0.25, 0.75])
# print(IQR)
# import seaborn as sns
# sns.boxplot(data['GRASS'])
