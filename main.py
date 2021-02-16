#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.matplotlib_fname()
plt.plot(np.random.rand(10), np.random.rand(10), label="legend")
plt.legend()
plt.show()
