# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:45:29 2018

@author: 後藤　嶺
"""

w1=1+3j

print(w1)
print(type(w1))

w2=1-3j

print(w1*w2)

w3=0+3j
w4=3j

if type(w3)==type(w4):
    print(str(w3)+"=="+str(w4))
    print("実部省略可能")
    print(type(w3+w4))
else:
    print(str(w3)+"!="+str(w4))
    print("実部省略不可")

w5=3+0j
w6=3
w7=w5+w6
if type(w5)==type(w6):
    print(str(w5)+"=="+str(w6))
    print("虚部省略可能だが明示的に省略しない")
else:
    print(str(w5)+"!="+str(w6))
    print("虚部省略可能だが計算はできる。そしてcomplex型になる")
    print(type(w7))



