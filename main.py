#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# plt.style.use('seaborn')
print(matplotlib.matplotlib_fname())
print(plt.style.available)
plt.plot(np.random.rand(10), np.random.rand(10), label="legend")
plt.xlabel("meter per seconds")
plt.ylabel("meter per yy")
plt.title("Title per yy")
plt.legend()
plt.show()
