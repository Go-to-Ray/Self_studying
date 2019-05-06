# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:17:18 2018

@author: 後藤　嶺
"""

import matplotlib.pyplot as mpl
import numpy as np
import math

x1=np.arange(-1,1.05,0.05)
x2=np.arange(-5,5.05,0.05)

#y1=np.cosh(x)
y2=np.sinh(x2)

#mpl.plot(x1,y1)
mpl.plot(x2,y2)

mpl.show()