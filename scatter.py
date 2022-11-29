import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("new.csv", encoding='gbk')
length = len(df)
unit_price = []
total_price = []
house_type = []
colors = {'商业类':'red', '写字楼':'green', '别墅':'blue', '住宅':'black', '商业':'pink'}
for i in range(length):
    if i != 36:
        unit_price.append(int(df['unit_price'][i]))
        total_price.append(int(df['total_price'][i]))
        house_type.append(str(df['house_type'][i]))
unit_price = np.array(unit_price)
total_price = np.array(total_price)

df = pd.DataFrame(dict(total_price=total_price, unit_price=unit_price, house_type = house_type))
fig, ax = plt.subplots()
grouped = df.groupby('house_type')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='total_price', y='unit_price', label=key, color=colors[key])
plt.grid(True, linestyle='--', alpha=0.8) 
plt.show()