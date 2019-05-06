# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:40:52 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import cis

fs = 8000
t = np.arange(0 ,2 ,1/fs)
pi = np.pi
a = 0.7
y523 = a*np.sin(2*pi*523*t)
y660 = a*np.sin(2*pi*660*t)
y784 = a*np.sin(2*pi*784*t)

yy = y523 + y660 + y784
cis.wavwrite('mixed_unnormalize.wav',yy,fs)
yy = yy/np.max(np.abs(yy))
cis.wavwrite('mixed_normalize.wav',yy,fs)

cis.audioplay(yy,fs)
r = np.arange(200)
plt.plot(t[r],yy[r])
plt.show()
