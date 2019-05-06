# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:34:20 2019

@author: 後藤　嶺
"""

import time
from itertools import product

target = "GFREAGVRE"
test_target = "p0ss"
chars = ["abcdefghijklmnopqrstuvwxyz",
         "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
         "1234567890"]

chars_selected = ""

#使う文字の選出
for i in range(3):
    k = int(input("1:小文字,2:大文字,3:数字,4:以上\n"))-1
    if 0<=k and k<=2:
        chars_selected += chars[k]
    else:
        break

pw_length_short = int(input("想定されるパスワードの長さを教えてください＞＞最短"))
pw_length_long  = int(input("想定されるパスワードの長さを教えてください＞＞最長"))



def check(chars,repeat):
    pws = product(chars,repeat=repeat)
    
    
    for pw in pws:
        print(pw)
        if "".join(pw) == test_target:
            return "".join(pw)

start = time.time()


for i in range(pw_length_short,pw_length_long+1):
    print(i,"の長さで検索中...")
    pw = check(chars_selected,i)
    if (pw is None):
        print("failure")
    else:
        print("got it! -->",pw)
        break

finish = time.time() - start
print(finish,"sec");
