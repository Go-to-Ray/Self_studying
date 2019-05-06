# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:00 2019

@author: 後藤　嶺
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as mlb

bar0 = np.zeros((500,100),np.uint8)
bar1 = 255*np.ones((500,100),np.uint8)
Col = np.zeros((500,800,3),np.uint8)
#RGB,Red==0,Green==1,Blue==2
#R255,R255,R0,R0,R255,R255,R0,R0
Col[:,:,0] = mlb.repmat(np.hstack((mlb.repmat(bar1,1,2),mlb.repmat(bar0,1,2))),1,2)
#G255,G255,G255,G255,G0,G0,G0,G0
Col[:,:,1] = np.hstack((mlb.repmat(bar1,1,4),mlb.repmat(bar0,1,4)))
#B255,B0,B255,B0,B255,B0,B255,B0
Col[:,:,2] = mlb.repmat(np.hstack((bar1,bar0)),1,4)
plt.imshow(Col)
plt.show()


'''
R255,R255,R0  ,R0  ,R255,R255,R0  ,R0
G255,G255,G255,G255,G0  ,G0  ,G0  ,G0
B255,B0  ,B255,B0  ,B255,B0  ,B255,B0
'''