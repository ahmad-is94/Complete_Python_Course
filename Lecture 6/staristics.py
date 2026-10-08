import statistics as st
from statistics import variance
from statistics import stdev
from statistics import harmonic_mean
from statistics import median
data = [1, 2, 3, 4, 5,6]
print("The mean of data is:", st.mean(data))
print("Median is:", median(data))
print("Mode of data is:", st.mode(data))
print("Low Median is:", st.median_low(data))
print("High Median is:", st.median_high(data))
print("Variance of data is:", variance(data))
print("Standard Deviation is:", stdev(data))
print("Harmonic mean is:", harmonic_mean(data))

values = [10, 15, 22, 27, 33]
largest = max(values)
smallest = min(values)
spread = largest - smallest
print("Maximum = {}, Minimum = {} and Range = {}".format(largest, smallest, spread))

#kde
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
data = np.random.normal(0, 1, 1000)
kde = gaussian_kde(data)
x = np.linspace(-4, 4, 100)
plt.plot(x, kde(x))
plt.show()