# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 23:04:28 2018

@author: 後藤　嶺
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.random import *

"""
操作量を求める.
サンプリング方式は
M = M1 + Kp*(e-e1) + Ki*e + Kd*{(e-e1) - (e1-e2)}
本来は
P：偏差(目的値と現在値の差)に比例した補正値を入力
  つまり偏差が小さくなるにつれ補正入力値が小さくなる
I:これまでの偏差の総和を足した値に比例した値を入力
D:偏差の傾きに比例する値を変えすことで、外乱（偏差のブレ）に対応できる
"""


M = 0.00
M1 = 0.00
goal = 50.00
e = 0.00
e1 = 0.00
e2 = 0.00
e_total =0.00
Kp = 1.5
Ki = 0.1
Kd = 0.1

t = 100      ##時間

x_list = []
y_list = []

x_list.append(0)
y_list.append(0.00)


##本文
for i in range(1,t):
    M1 = M
    e1 = e
    e2 = e1
    e_total += e
    e = goal - y_list[i-1] #偏差(e) = 目的地(goal) - 前回までの合計操作量
    
    M = M1 + Kp*e + Ki*(e+e1+e2) + Kd*((e-e1) - (e1-e2))
##  M = M1 + Kp*e + Ki * e_total + Kd*((e-e1) - (e1-e2))
    #微分積分についてはCでやった数値解析の問題を使えばいいのでは？
    #さらにKp,Ki,Kdを機械学習で求めることができるのではないか？
    
    x_list.append(i)
    y_list.append(M)

plt.plot(x_list,y_list)
plt.ylim(0,goal*2)
plt.show()
print(y_list[t-1])