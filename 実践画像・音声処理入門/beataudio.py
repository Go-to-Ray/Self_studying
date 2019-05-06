# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:44:26 2019

@author: 後藤　嶺
"""

#beat(うなり)audio(4times/s)

import numpy as np
import matplotlib.pyplot as plt
import cis

fs = 8000
t = np.arange(0 ,2 ,1/fs)
pi = np.pi
a = 0.5
y442 = a*np.sin(2*pi*442*t)
y438 = a*np.sin(2*pi*438*t)
yy = y438 + y442

y_y = np.hstack((y438,y442,yy))

cis.audioplay(y_y,fs)
r = np.arange(2000)
plt.plot(t[r],yy[r])
plt.show()
