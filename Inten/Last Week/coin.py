import numpy as np
import collections

def conf_int(p0,p1,z,n):
    temp=z*np.sqrt((p0*p1)/n)
    return temp

count=0
for i in range(100):

    trials=10000
    a=np.random.randint(0,2,size=trials)

    a=list(a)
    p0=a.count(0)/trials
    p1=a.count(1)/trials

    #print(p0,p1)
    val_low=p1-conf_int(p0,p1,1.96,trials)
    val_hi=p1+conf_int(p0,p1,1.96,trials)
    if (val_low)<0.5 and  (val_hi)>0.5:
        count=count+1

#print(p1-conf_int(p0,p1,1.96,trials),p1+conf_int(p0,p1,1.96,trials))
#print(p0,p1,conf_int(p0,p1,19.6,trials)\)
print(count,"%")