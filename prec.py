#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

Precip = pd.read_csv('precip.csv', sep=',', index_col='YYYYMMDD')

dates = pd.date_range('20000101', periods=len(Precip.index))
df1 = Precip.reindex(index=dates, columns=list(Precip.columns))

freq = [] #lista que almacenará los días que llueve más de 1mm por estación
          #fre[0] almacenará los días que ha llovido más de 1mm en la primera estación
for i in range(0,len(df1.columns)):
    freq.append(sum(df1.iloc[:,i].values.astype(float) > 1))

#hacemos el plot de estas frecuencias
labels = list(df1.columns.astype(int))      #nombres de las estaciones
x = range(0, len(df1.columns.astype(int)))  #posiciones en el eje x de los nombres de las estaciones
y = freq

fig, ax = plt.subplots(figsize=(18,5))

ax.bar(x, y)
ax.set_xticks([idx+0.5 for idx in range(len(labels))])          #posiciones de las etiquetas
ax.set_xticklabels(labels, rotation=80, ha='right', size=10)    #ponemos los nombres de las etiquetas en las posiciones

plt.xlabel('Station')
plt.ylabel('Frequency (rain > 1 mm)')
fig.savefig('frec.png')
plt.show()

