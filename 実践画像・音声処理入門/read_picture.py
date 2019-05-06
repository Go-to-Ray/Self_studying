# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 05:01:31 2019

@author: 後藤　嶺
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as mlb
import cv2
import cis

I = cv2.imread('picture data/NieR_display.png')
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))
plt.show()

Ired = cv2.imread('picture data/redpepper.jpg')
h,w,b = Ired.shape
I = cv2.imread('picture data/paprika-966290_1280.jpg')
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))
plt.show()

Iyellow = I[155:155+h,390:390+w]
plt.imshow(cv2.cvtColor(Iyellow,cv2.COLOR_BGR2RGB))
plt.show()
Imixed = Iyellow/2 + Ired/2
Imixed = Imixed.astype(np.uint8)
plt.imshow(cv2.cvtColor(Imixed,cv2.COLOR_BGR2RGB))
plt.show()