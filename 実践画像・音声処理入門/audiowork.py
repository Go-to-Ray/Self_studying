# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:33:35 2019

@author: 後藤　嶺
"""

#audiowork

import cis
import numpy as np
import matplotlib.pyplot as plt
import math


fs = 16000
t = np.arange(0,0.5,1/fs)
y = np.sin(2*np.pi*523*t)

r=np.arange(math.ceil(16000/523))
plt.plot(t[r],y[r])

cis.audioplay(y,fs)