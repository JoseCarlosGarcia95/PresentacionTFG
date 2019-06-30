#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

data_to_plot = {
    "C": {
        "time": [0.001, 0.001, 0.001, 0.001, 0.001, 0.005, 1.179, 8.961, 22.99],
        "energy": [0.1, 0.1, 0.1, 0.1, 0.1, 0.005, 117.8, 896.1, 2299]
    },
    "Parallel": {
        "time": [0.001, 0.001, 0.001, 0.001, 0.001, 0.005, 0.624, 7.754, 9.227],
        "energy": [0.23, 0.23, 0.23, 0.23, 0.23, 1.15, 143.52, 1783.42, 2122.21]
    },
    "GPU" : {
        "time": [0.441, 0.441, 0.441, 0.441, 0.484, 0.472, 0.997, 2.595, 3.221],
        "energy": [57.33, 57.22, 57.33, 57.33, 62.92, 61.36, 129.61, 337.22, 418.73]
    }

}

x = np.array([5, 25, 50, 70, 100, 1000, 10000, 20000, 22760])
xs = np.linspace(5, 22760, 3000)

for label, data in data_to_plot.items():
    y = data['energy']
    plt.plot(x, y, label=label)

plt.legend()
plt.show()
