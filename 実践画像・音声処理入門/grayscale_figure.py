# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 03:56:31 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(255,0,12)
print(x)
x = x.astype(np.uint8)
print(x)
x = x.reshape(3,4)
print(x)

plt.imshow(x,cmap='gray')
plt.show()