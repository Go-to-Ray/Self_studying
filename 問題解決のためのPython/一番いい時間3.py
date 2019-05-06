# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:54:59 2018

@author: 後藤　嶺
"""
ystart,yend = int(input()),int(input())
yoursched=(ystart,yend)

sched2 = [(6.0,8.0,1),(6.5,12.0,1),(6.5,7.0,1),(7.0,8.0,1),
          (7.5,10.0,1),(8.0,9.0,1),(8.0,10.0,1),(9.0,12.0,1),
          (9.5,10.0,1),(10.0,11.0,1),(10.0,12.0,1),(11.0,12.0,1)]
sched3 = [(6.0,8.0,2),(6.5,12.0,1),(6.5,7.0,2),(7.0,8.0,2),
          (7.5,10.0,3),(8.0,9.0,2),(8.0,10.0,1),(9.0,12.0,2),
          (9.5,10.0,4),(10.0,11.0,2),(10.0,12.0,3),(11.0,12.0,7)]
def bestTimeToPartySmart(schedule,yourschedule):
    times = []
    
    for c in schedule:
        if yourschedule[0]<c[1] or yourshedule[1]>c[0]:
            times.append((c[0],'start',c[2]))
            times.append((c[1],'end',c[2]))
    """
    for c in schedule:
        if yourschedule[0]<c[1]:
            times.append((c[0],'start'))
            times.append((c[1],'end'))
        else:
            break
    for c in schedule[::-1]:
        if yourschedule[1]>c[0]:
            times.append((c[0],'start'))
            times.append((c[1],'end'))
        else:
            break
    """
    sortList(times)
    maxcount, time = chooseTime(times)
    print('Best time to attend the party is at',time,'o\'clock',
          ':',maxcount,'weight of celebrities will be attending!')
    

def sortList(tlist):
    for ind in range(len(tlist)-1):#ind=0~22
        iSm = ind
        for i in range(ind,len(tlist)):#i=ind~23
            if tlist[iSm][0] > tlist[i][0]:
                iSm = i
        tlist[ind],tlist[iSm] = tlist[iSm],tlist[ind]

def chooseTime(times):
    rcount = 0
    maxcount = time = 0
    for t in times:
        if t[1] == 'start':
            rcount += t[2]
        elif t[1] == 'end':
            rcount -= t[2]
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
    return maxcount,time

bestTimeToPartySmart(sched2,yoursched)
bestTimeToPartySmart(sched3,yoursched)