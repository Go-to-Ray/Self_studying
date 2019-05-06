# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 04:47:31 2018

@author: 後藤　嶺
"""

sched = [(6,8),(6,12),(6,7),(7,8),(7,10),(8,9),
         (8,10),(9,12),(9,10),(10,11),(10,12),(11,12)]

def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    #partyの開始時刻と終了時刻の検索
    for c in schedule:
        start = min(c[0],start)
        end = max(c[1],end)
    count = celebrityDensity(schedule,start,end)
    '''
    maxcount = 0
    for i in range(start,end + 1):
        if count[i] > maxcount:
            maxcount = count[i]
            time = i
            '''
    maxcount = max(count[start:end + 1]) #count配列のstart~end+1までで最大値を抽出
    time = count.index(maxcount) #countでmaxcountのあるインデックスをtimeに初期化
    print("Best time to attend the party is at",time,"o\'clock",
          ":",maxcount,"celebrities will be attending!")

#メインコード
def celebrityDensity(sched,start,end):
    count = [0]*(end + 1)
    for i in range(start,end + 1):
        count[i] = 0
        for c in sched:
            if c[0]<=i and c[1]>i:
                count[i] += 1
    return count

bestTimeToParty(sched)