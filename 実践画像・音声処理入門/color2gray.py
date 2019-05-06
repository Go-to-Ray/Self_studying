# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:18:58 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as mlb
import cv2
import cis

C = cv2.imread("picture data/coins-1466263_1280.jpg")
G = cv2.cvtColor(C, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(C,cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(G,cmap="gray")
plt.show()

C2 = cv2.cvtColor(C,cv2.COLOR_BGR2RGB)
BW = np.zeros(G.shape)    #抽出のための媒介変数みたいなもん
BW[G>125] = 1    #明るさ125を超える画素を抽出
R = C2.copy()
R[BW==0] = 0    #抽出されて残った場所を黒にする
plt.imshow(R)
plt.show()