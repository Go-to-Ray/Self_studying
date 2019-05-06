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

y1_odd=0
y1_even=-pi/2
y2=pi/4
f3=0
g3=0
##blue_line 問題１
for i in range(1,1000):
    y1_odd+=2*(-1)**i*np.sin(i*x)/i
    y1_even+=2*(1-(-1)**i)*np.cos(i*x)/(i**2*pi)
y1=(y1_odd+y1_even)/2
##orange_line　問題２
for j in range(1,1000):
    y2+=((1-(-1)**(j))*np.cos(j*x)/(j**2)/pi+np.sin(j*x)/j)
##green_line 問題３のｆ（ｘ）
for k in range(1,1000):
    f3+=4*np.sin(k*pi/2)*np.sin(k*x)/(k**2*pi)
##red_line 問題３のｇ（ｘ）
for n in range(1,1000):
    g3+=4*np.sin(n*pi/2)*np.cos(n*x)/(n*pi)
    


mpl.plot(x,y1)
mpl.plot(x,y2)
mpl.plot(x,f3)
mpl.plot(x,g3)


mpl.show()