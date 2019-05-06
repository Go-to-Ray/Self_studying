# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 03:55:27 2018

@author: 後藤　嶺
"""

cap1=["F","F","B","B","B","F","B","B","B","F","F","B","F"]
cap2=["F","F","B","B","B","F","B","B","B","F","F","F","F"]
cap3=[]
cap4=["F"]
cap5=["F","F"]
cap6=["B","F","B"]
cap7=['F','F','B','H','B','F','B','B','B','F','H','F','F']
def pleaseConform(caps):
    start = forward = backward = 0
    intervals =[]
    for i in range(1,len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start,i-1,caps[start]))#タプルを配列に追加
            #print(intervals)
            if caps[start] == "F":
                forward += 1
            else:
                backward += 1
            start = i
    #最後の帽子情報を追加
    intervals.append((start,len(caps)-1,caps[start]))
    #print(intervals)
    if caps[start] == "F":
        forward += 1
    else:
        backward += 1
    #最小限の掛け声にするための条件式
    if forward < backward:
        flip = "F"
    else:
        flip = "B"
    #配列からタプルを取り出して出力する
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print("People in positions",t[0],"flip your caps!")
            else:
                print("People in positions",t[0],
                      "through",t[1],"flip your caps!")

#上のプログラムと全く同じ
def pleaseConformOnepass(caps):
    if caps == []:
        print('There is not menber...')
    elif len(caps)==1:
        print('There is a menber')
    elif True == all([cap==caps[0] for cap in caps[1:]]):
        print("All persons is completed!!")
    else:        
        caps = caps + [caps[0]]
        for i in range(1,len(caps)):
            if caps[i] != caps[i-1]:
                if (caps[i-1] != caps[i]) & (caps[i] != caps[i+1]) & (caps[i]!=caps[0]):
                    if (caps[i] != caps[0]) & (caps[i] != 'H'):
                        print('person at position',i,'flip your cap!')
                else:
                    if caps[i] != caps[0]:#一番目が前なら最小の呼びかけは後ろになるから
                        print('People in positions',i,end="")
                    elif (caps[i-2] != caps[i-1]) & (caps[i-1] != caps[i]) & (caps[i-1]!=caps[0]):
                        pass
                    else:
                        print(' through',i-1,'flip your caps!')

print("cap1")
pleaseConformOnepass(cap1)
print("cap2")
pleaseConformOnepass(cap2)
print("cap3")
pleaseConformOnepass(cap3)
print("cap4")
pleaseConformOnepass(cap4)
print("cap5")
pleaseConformOnepass(cap5)
print("cap6")
pleaseConformOnepass(cap6)
print('cap7')
pleaseConformOnepass(cap7)