import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read in the data
df = pd.read_csv("Stock3.csv")
df_2 = pd.read_csv("tst.csv", skiprows=1)

# extract the relevant columns
price = df_2.iloc[:, 1]
prediction = df.iloc[:, 1]

# create a scaled version of the prediction
scaled_prediction = prediction * max(price) / max(prediction)

# create a scaled version of the price values
scaled_price = price * max(scaled_prediction) / max(price)

# compute the cross-correlation
corr = np.correlate(scaled_price, scaled_prediction, mode='same')
corr_value = np.max(corr)

# plot the data
fig, ax1 = plt.subplots()
ax1.plot(scaled_price, color='blue', label='Price')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(prediction, color='red', label='Prediction')
ax2.plot(scaled_prediction, color='green', label='Scaled Prediction')
ax2.set_ylabel('Prediction', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# print the cross-correlation value
print(f"Cross-correlation value: {corr_value:.2f}")

plt.title("Long Slong Stock")
plt.legend(loc='upper left')
plt.show()
