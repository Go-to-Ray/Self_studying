# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:36:50 2018

@author: 後藤　嶺
"""

data1=["B","W","W","W","W","W","B","W","W","W","W"]
data2="BWWWWWBWWWW"

'''
def judge_type(datas):
    if type(datas) == type(""):
        datas = list(datas)
        code = []　　　　　　　　　　　　　　　　　　　　　　←ココから
        datas += ["end"]
        count = 1
        for i in range(len(datas)-1):
            if datas[i] == datas[i+1]:
                count += 1
            else:
                code.append(str(count))
                code.append(datas[i])
                count = 1
        for k in code:
            print(k,end="")　　　　　　　　　　　　　←ココまで　と
    else:
        code = []　　　　　　　　　　　　　　　　　　　　　　←ココから
        datas += ["end"]
        count = 1
        for i in range(len(datas)-1):
            if datas[i] == datas[i+1]:
                count += 1
            else:
                code.append(str(count))
                code.append(datas[i])
                count = 1
        for k in code:
            print(k,end="")　　　　　　　　　　　　←ココまで　が同じなので下の関数のように変えてみる
            
'''


judge_type(data1)
print()
judge_type(data2)

##入力がリスト型の場合のランレング符号化関数(メインコード)
def runlength(datas):
    code = []
    datas += ["end"]
    count = 1
    for i in range(len(datas)-1):
        if datas[i] == datas[i+1]:
            count += 1
        else:
            code.append(str(count))
            code.append(datas[i])
            count = 1
    for k in code:
        print(k,end="")

#入力がｓｔｒ型でも動くように条件分岐させた後に上の関数を呼び出す        
def judge_type(datas):
    if type(datas) == type(""):
        datas = list(datas)
        runlength(datas)
    else:
        runlength(datas)