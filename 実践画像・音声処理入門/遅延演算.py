# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 02:52:23 2019

@author: 後藤　嶺
"""

import numpy as np
import cis
import matplotlib.pyplot as plt


fs = 8000
t = np.arange(0,1,1/fs)
s = np.sin(2*np.pi*800*t) + np.sin(2*np.pi*500*t)
#cis.audioplay(s,fs)
rg = np.arange(0,100)
#plt.subplot(7,1,1);plt.plot(s[rg])

sd = np.roll(s,5)
#cis.audioplay(sd,fs)
#plt.subplot(7,1,2);plt.plot(sd[rg])

ssd = s + sd
#cis.audioplay(ssd,fs)
#plt.subplot(7,1,3);plt.plot(ssd[rg])


#白色雑音の生成
r = np.random.standard_normal(t.shape)
r = 0.8*r/np.max(np.abs(r))    #正規化
n = np.arange(0,100)
#plt.subplot(7,1,4);plt.plot(t[n],r[n])
#cis.audioplay(r,fs)


s = np.sin(2*np.pi*440*t)
sn = 0.8*s+0.25*r
#plt.subplot(7,1,5);
plt.plot(t[n],sn[n],t[n],0.8*s[n])
cis.audioplay(sn,fs)