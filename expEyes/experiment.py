import sys, time, utils, math, os.path

from QtVersion import *
from PyQt5.QtCore import *

import pyqtgraph as pg
import numpy as np
import eyes17.eyemath17 as em
import math

try:
	import pandas as pd
except:
	os.system('pip install pandas')
	import pandas as pd
	
import matplotlib.pyplot as plt
import platform

df = pd.read_csv('rc1.csv', header=None, skiprows=1)
df = df.dropna(axis=1)
cols = df.shape[1]
history = []
for i in range(0, cols, 2):
	history.append((df.iloc[:, i], df.iloc[:, i+1]))

print(history[-1][0], history[-1][1])
fa = em.fit_exp(history[-1][0], history[-1][1])
#fa = em.fit_exp(19.96, 4.321488276)
pa = fa[1]
rc = abs(1.0 / pa[1])
print(rc)

xs = []
ys = []
for i in range(0, cols, 2):
	xs.append(df.iloc[:, i])
	ys.append(df.iloc[:, i+1])
	
def plotting(X_values, Y_values, v_c, v_d):
		plt.figure(figsize=(7,6))
		plt.title("RC Transient response Experiment")
		plt.xlabel("Time (seconds)")
		plt.ylabel("Voltage (V)")
		plt.grid()
		i = 0
		for x, y in zip(X_values, Y_values):
			plt.plot(x, y, label=str(i))
			plt.legend(loc='best', frameon=False, borderaxespad=0)
			i += 1
		plt.plot(0, v_c, "ro", markersize=3)
		plt.plot(0, v_d, "bo", markersize=3)
		plt.show()
	
t = df.iloc[-1, 0]
print(t)
v_charge = 5 * (1-(math.exp(-t/rc)))
v_dis = 5 * (math.exp(-t/rc))
plotting(xs, ys, v_charge, v_dis)

