import matplotlib.pyplot as plt
import numpy as np

ys = [30]
xs = range(0, 501)
np.random.seed(seed=42)
for delta in np.random.normal(0, 0.5, 500):
    ys.append(ys[-1] + delta)

plt.plot(ys)
plt.ylabel('Stock Price ($)')
plt.xlabel('Elapsed Time (min)')
plt.savefig('C:\\workspace\\1.01.svg')
