# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:27:50 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as mlb
import cv2
import cis

C = cv2.imread("picture data/paprika-966290_1280.jpg")
C = cv2.cvtColor(C,cv2.COLOR_BGR2RGB)
plt.imshow(C)
plt.show()
BW = np.zeros((C.shape[0],C.shape[1]))
BW[np.logical_and(np.logical_and(np.logical_and(C[:,:,0]>150,C[:,:,0]<240),\
                                 np.logical_and(C[:,:,1]>80,C[:,:,1]<220)),C[:,:,2]<40)]=1
R = C.copy()
R[BW==0]=0
plt.imshow(R)
plt.show()

Y = C[464:704,836:1106]
print(np.max(np.max(Y,1),0))    #行のなかで最大(明るい)の配列を抽出してから、列の中で最大のものを拾ってくる。全てのRGBの最大値を入手できる
print(np.max(np.max(Y,0),0))    #特定の列で一番明るい行を並べて、またその中から最も明るい値を入手して存在するかもしれない、最も明るいRGB配列を作る
print(np.min(np.min(Y,0),0))
Y_max = np.max(np.max(Y,1),0)
Y_max = np.clip(Y_max + Y_max*0.1,0,255)
                
Y_min = np.min(np.min(Y,1),0)
Y_min = np.clip(Y_min - Y_min*0.1,0,255)

BW = np.zeros((C.shape[0],C.shape[1]))
BW[np.logical_and(np.logical_and(np.logical_and(C[:,:,0]>=Y_min[0],C[:,:,0]<=Y_max[0]),\
                                 np.logical_and(C[:,:,1]>=Y_min[1],C[:,:,1]<=Y_max[1])),\
                                 np.logical_and(C[:,:,2]>=Y_min[2],C[:,:,2]<=Y_max[2]))]=1
R = C.copy()
R[BW==0]=0
plt.imshow(R)
plt.show()