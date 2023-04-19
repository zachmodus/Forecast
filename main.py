import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("Stock2.csv")

df_2 = pd.read_csv("tst.csv", skiprows=1)

data = df.iloc[:, 1]
data_2 = df_2.iloc[:, 1]

data = np.array(data)
data_2 = np.array(data_2)
data_3 = 110 * np.array(data)

"""

plt.plot(data, label='no change')


plt.plot(data_3, label='scaled')
plt.legend(loc='lower right')
plt.show()
'''

"""
plt.title("Long Slong Stock")

plt.subplot(3,1,1)
plt.plot(data, label='prediction')
plt.legend(loc='lower right')


plt.subplot(3,1,2)
plt.plot(data_2, label='no change')
plt.legend(loc='lower right')


plt.subplot(3,1,3)
plt.plot(data_3, label='scaled')
plt.legend(loc='lower right')
plt.show()

"""

fig, ax1 = plt.subplots()

# plot y1 on ax1
ax1.plot(data_2, color='blue')
ax1.set_xlabel('x')
ax1.set_ylabel('y1', color='blue')

# create the second plot
ax2 = ax1.twinx()

# plot y2 on ax2
ax2.plot(data, color='red')
ax2.set_ylabel('y2', color='red')

# show the plot
plt.show()

"""
