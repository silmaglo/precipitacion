{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "Precip = pd.read_csv('precip.csv', sep=',', index_col='YYYYMMDD')\n",
    "\n",
    "dates = pd.date_range('20000101', periods=len(Precip.index))\n",
    "df1 = Precip.reindex(index=dates, columns=list(Precip.columns))\n",
    "\n",
    "freq = [] #lista que almacenará los días que llueve más de 1mm por estación\n",
    "          #fre[0] almacenará los días que ha llovido más de 1mm en la primera estación\n",
    "for i in range(0,len(df1.columns)):\n",
    "    freq.append(sum(df1.iloc[:,i].values.astype(float) > 1))\n",
    "\n",
    "#hacemos el plot de estas frecuencias\n",
    "labels = list(df1.columns.astype(int))      #nombres de las estaciones\n",
    "x = range(0, len(df1.columns.astype(int)))  #posiciones en el eje x de los nombres de las estaciones\n",
    "y = freq\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(18,5))\n",
    "\n",
    "ax.bar(x, y)\n",
    "ax.set_xticks([idx+0.5 for idx in range(len(labels))])          #posiciones de las etiquetas\n",
    "ax.set_xticklabels(labels, rotation=80, ha='right', size=10)    #ponemos los nombres de las etiquetas en las posiciones\n",
    "\n",
    "plt.xlabel('Station')\n",
    "plt.ylabel('Frequency (rain > 1 mm)')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
