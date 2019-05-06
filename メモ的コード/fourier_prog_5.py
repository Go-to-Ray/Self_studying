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

for i in range(1,10000):
    y1_odd+=2*(-1)**i*np.sin(i*x)/i
    y1_even+=2*(1-(-1)**i)*np.cos(i*x)/(i**2*pi)
    ##orange_line　問題２
    y2+=((1-(-1)**(i))*np.cos(i*x)/(i**2)/pi+np.sin(i*x)/i)
    ##green_line 問題３のｆ（ｘ）
    f3+=4*np.sin(i*pi/2)*np.sin(i*x)/(i**2*pi)
    ##red_line 問題３のｇ（ｘ）
    g3+=4*np.sin(i*pi/2)*np.cos(i*x)/(i*pi)
##blue_line 問題１
y1=(y1_odd+y1_even)/2
    
mpl.plot(x,y1)
mpl.plot(x,y2)
mpl.plot(x,f3)
mpl.plot(x,g3)

mpl.show()