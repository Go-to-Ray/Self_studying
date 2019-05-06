# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:01:11 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as mlb
import cv2
import cis

cap = cv2.VideoCapture('picture data/636795321.m4v')
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
nFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

frame = np.zeros((height,width,3,nFrame),np.uint8)

for k in range(0,frame.shape[3]):
    ret, f = cap.read()  #retにはtrue/falseを返して、fに各フレームのframe配列を返す
    if ret:
        frame[:,:,:,k] = f
        k += 1
        """
        continue
    break
    #is this scripts needed??
    """
cis.implay(frame)
cv2.destroyAllWindows()
cv2.imshow('frame0',frame[:,:,:,0])
cv2.imshow('frame1000',frame[:,:,:,1000])
cv2.destroyAllWindows()