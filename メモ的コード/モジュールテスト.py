# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:35:26 2018

@author: 後藤　嶺
"""

import matplotlib.pyplot as mpl
import numpy as np
import math
pi = math.pi

x=np.arange(-10,10,0.01)

y=0
ya=pi/4
yb=0
yc=0
for i in range(1,1000):
    y+=4*np.sin(i*pi/2)*np.sin(i*x)/(i**2*pi)
    
for j in range(1,1000):
    ya+=((1-(-1)**(j))*np.cos(j*x)/(j**2)/pi+np.sin(j*x)/j)
    
for k in range(1,1000):
    yb+=(-2)*(-1)**(k)*np.sin(k*x)/k
    
for n in range(1,1000):
    yc+=4*np.sin(n*pi/2)*np.cos(n*x)/n/pi
    


mpl.plot(x,y)
mpl.plot(x,ya)
mpl.plot(x,yb)
mpl.plot(x,yc)


mpl.show()