import numpy as np
from numba import jit,vectorize
from scipy.stats import ortho_group
import time
import pandas as pd
import cupy as cp

t1=time.time()
runge=1000
p=np.arange(0,0.51,0.01).astype(np.float32)
'''
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])
'''
x1=[]
x2=[]
x3=[]
y1=cp.array([1,0,0]).astype(np.float32)
y2=cp.array([0,1,0]).astype(np.float32)
y3=cp.array([0,0,1]).astype(np.float32)

for i in range(runge):
    l=ortho_group.rvs(3)
    x1.append(l[0])
    x2.append(l[1])
    x3.append(l[2])
    
x1=cp.array(x1).astype(np.float32)
x2=cp.array(x2).astype(np.float32)
x3=cp.array(x3).astype(np.float32)

t2=time.time()
print(t2-t1)

temp=[i for i in range(36)]
a=cp.array(temp)
arr=[]
r=[]

for i in p:
    tn1=time.time()
    E11=-2*cp.sqrt(i-i**2)*cp.dot(x1,y1)
    E21=-2*cp.sqrt(i-i**2)*cp.dot(x2,y1)
    E31=-2*cp.sqrt(i-i**2)*cp.dot(x3,y1)
    
    E12=2*cp.sqrt(i-i**2)*cp.dot(x1,y2)
    E22=2*cp.sqrt(i-i**2)*cp.dot(x2,y2)
    E32=2*cp.sqrt(i-i**2)*cp.dot(x3,y2)
    
    E13=cp.dot(x1,y3)
    E23=cp.dot(x2,y3)
    E33=cp.dot(x3,y3)
    
    a0=cp.asnumpy((abs(+E11+E12+E21-E22)))
    a1=cp.asnumpy((abs(+E11+E12-E21+E22)))
    a2=cp.asnumpy((abs(+E11-E12+E21+E22)))
    a3=cp.asnumpy((abs(-E11+E12+E21+E22)))

    a4=cp.asnumpy((abs(+E11+E13+E21-E23)))
    a5=cp.asnumpy((abs(+E11+E13-E21+E23)))
    a6=cp.asnumpy((abs(+E11-E13+E21+E23)))
    a7=cp.asnumpy((abs(-E11+E13+E21+E23)))
                                    
    a8=cp.asnumpy((abs(+E12+E13+E22-E23)))
    a9=cp.asnumpy((abs(+E12+E13-E22+E23)))
    a10=cp.asnumpy((abs(+E12-E13+E22+E23)))
    a11=cp.asnumpy((abs(-E12+E13+E22+E23)))
                                
    a12=cp.asnumpy((abs(+E11+E12+E31-E32)))
    a13=cp.asnumpy((abs(+E11+E12-E31+E32)))
    a14=cp.asnumpy((abs(+E11-E12+E31+E32)))
    a15=cp.asnumpy((abs(-E11+E12+E31+E32)))
                                
    a16=cp.asnumpy((abs(+E11+E13+E31-E33)))
    a17=cp.asnumpy((abs(+E11+E13-E31+E33)))
    a18=cp.asnumpy((abs(+E11-E13+E31+E33)))
    a19=cp.asnumpy((abs(-E11+E13+E31+E33)))
                    
    a20=cp.asnumpy((abs(+E12+E13+E32-E33)))
    a21=cp.asnumpy((abs(+E12+E13-E32+E33)))
    a22=cp.asnumpy((abs(+E12-E13+E32+E33)))
    a23=cp.asnumpy((abs(-E12+E13+E32+E33)))
                        
    a24=cp.asnumpy((abs(+E21+E22+E31-E32)))
    a25=cp.asnumpy((abs(+E21+E22-E31+E32)))
    a26=cp.asnumpy((abs(+E21-E22+E31+E32)))
    a27=cp.asnumpy((abs(-E21+E22+E31+E32)))
                                        
    a28=cp.asnumpy((abs(+E21+E23+E31-E33)))
    a29=cp.asnumpy((abs(+E21+E23-E31+E33)))
    a30=cp.asnumpy((abs(+E21-E23+E31+E33)))
    a31=cp.asnumpy((abs(-E21+E23+E31+E33)))
                                                            
    a32=cp.asnumpy((abs(+E22+E23+E32-E33)))
    a33=cp.asnumpy((abs(+E22+E23-E32+E33)))
    a34=cp.asnumpy((abs(+E22-E23+E32+E33)))
    a35=cp.asnumpy((abs(-E22+E23+E32+E33)))
    tn2=time.time()
    print('tn',tn2-tn1)
    bellu=np.array([a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35]).astype(np.float32)
    bellu=(bellu.T)
    bell=cp.array(bellu)
    '''
    x = cp.amax(bell, 1)
    count=runge
    for j in x:
        if j<2:
            count=count-1
    arr.append(count/runge)
    r.append(runge)
    '''
'''
df=pd.DataFrame({'P':p,'Prob':arr,'No. Measure':r})

df.to_excel(r'output5.xlsx')
t3=time.time()
print(tn2-t2) 
  


def fn(p,a1,a2,a3,b1,b2,b3):
return p*a3*b3 + (1-p)*a3*b3 - 2*np.sqrt(p-p**2)*(a1*b1-a2*b2)
'''