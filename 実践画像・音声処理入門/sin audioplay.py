# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:27:15 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import cis

t=np.arange(0,1,1/8000)
a=0.8
f=440
y=a*np.sin(2*np.pi*f*t)

cis.audioplay(y,8000)

plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitube')
plt.show()
