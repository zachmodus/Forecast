import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read in the data
df = pd.read_csv("Needswork2.csv")
df_2 = pd.read_csv("predictivevalue2.csv", skiprows=1)

# extract the relevant columns
price = df_2.iloc[:, 1]
prediction = df.iloc[:, 1]

# create a scaled version of the prediction
scaled_prediction = 110 * prediction

# plot the data
fig, ax1 = plt.subplots()
ax1.plot(price, color='blue', label='Price')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(prediction, color='red', label='Prediction')
ax2.plot(scaled_prediction, color='green', label='Scaled Prediction')
ax2.set_ylabel('Prediction', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title("Long Slong Stock")
plt.legend(loc='upper left')
plt.show()
