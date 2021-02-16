#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

print(plt.style.available)
plt.style.use('doomeone')
print(matplotlib.matplotlib_fname())
plt.plot(np.random.rand(10), np.random.rand(10), label="legend")
plt.plot(np.random.rand(10), np.random.rand(10), label="legend")
plt.plot(np.random.rand(10), np.random.rand(10), label="legend")
plt.xlabel("meter per seconds")
plt.ylabel("meter per yy")
plt.title("Title per yy")
plt.legend()
plt.show()
