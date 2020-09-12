import numpy as np
from numba import jit,vectorize
from scipy.stats import ortho_group
import time
import pandas as pd

t1=time.time()
p=np.arange(0,1.01,0.01)
runge=1000000
a=[]
for i in range(runge):
    x=ortho_group.rvs(3)
    a.append(x)

a=np.array(a).astype('float32')
#print(a.shape)
t2=time.time()
print(t2-t1)



b1=np.array([1,0,0]).astype('float32')
b2=np.array([0,1,0]).astype('float32')
b3=np.array([0,0,1]).astype('float32')


#@vectorize(['int32(int32, int32)'], target='cuda')
def add_ufunc(a, b1, b2, b3, p):
    E_1= -np.dot(a,b1)-p*np.dot(a,b1)
    E_1=E_1.T
    E_1=E_1/(1+p)
    
    E_2= -np.dot(a,b2)+p*np.dot(a,b2)
    E_2=E_2.T
    E_2=E_2/(1+p)
    
    E_3= -np.dot(a,b3)+p*np.dot(a,b3)
    E_3=E_3.T
    E_3=E_3/(1+p)
    
    E11=E_1[0]
    E21=E_1[1]
    E31=E_1[2]
    E12=E_2[0]
    E22=E_2[1]
    E32=E_2[2]
    E13=E_3[0]
    E23=E_3[1]
    E33=E_3[2]
    
    
    a0=(abs(+E11+E12+E21-E22))
    a1=((abs(+E11+E12-E21+E22)))
    a2=((abs(+E11-E12+E21+E22)))
    a3=((abs(-E11+E12+E21+E22)))
    
    a4=((abs(+E11+E13+E21-E23)))
    a5=((abs(+E11+E13-E21+E23)))
    a6=((abs(+E11-E13+E21+E23)))
    a7=((abs(-E11+E13+E21+E23)))
                                   
    a8=((abs(+E12+E13+E22-E23)))
    a9=((abs(+E12+E13-E22+E23)))
    a10=((abs(+E12-E13+E22+E23)))
    a11=((abs(-E12+E13+E22+E23)))
                              
    a12=((abs(+E11+E12+E31-E32)))
    a13=((abs(+E11+E12-E31+E32)))
    a14=((abs(+E11-E12+E31+E32)))
    a15=((abs(-E11+E12+E31+E32)))
                               
    a16=((abs(+E11+E13+E31-E33)))
    a17=((abs(+E11+E13-E31+E33)))
    a18=((abs(+E11-E13+E31+E33)))
    a19=((abs(-E11+E13+E31+E33)))
                   
    a20=((abs(+E12+E13+E32-E33)))
    a21=((abs(+E12+E13-E32+E33)))
    a22=((abs(+E12-E13+E32+E33)))
    a23=((abs(-E12+E13+E32+E33)))
                     
    a24=((abs(+E21+E22+E31-E32)))
    a25=((abs(+E21+E22-E31+E32)))
    a26=((abs(+E21-E22+E31+E32)))
    a27=((abs(-E21+E22+E31+E32)))
                                     
    a28=((abs(+E21+E23+E31-E33)))
    a29=((abs(+E21+E23-E31+E33)))
    a30=((abs(+E21-E23+E31+E33)))
    a31=((abs(-E21+E23+E31+E33)))
                                                         
    a32=((abs(+E22+E23+E32-E33)))
    a33=((abs(+E22+E23-E32+E33)))
    a34=((abs(+E22-E23+E32+E33)))
    a35=((abs(-E22+E23+E32+E33)))
    bell=np.array([a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35])
    bell=(bell.T)                                                       
    return bell



#print(abs(d[0]))
c=[]
r=[]
for i in p:
    d=add_ufunc(a,b1,b2,b3,i)
    count=runge
    for j in d:
        if max(j)<2:
            count=count-1
    c.append(count/runge)
    r.append(runge)
    print(i,count/runge)
t3=time.time()
#print(t3-t2,minn)

df=pd.DataFrame({'P':p,'Prob':c,'No. Measure':r})

df.to_excel(r'output2.xlsx')