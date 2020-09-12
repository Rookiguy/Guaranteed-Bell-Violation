import numpy as np
from numba import jit,vectorize
from scipy.stats import ortho_group
import time
import pandas as pd

t1=time.time()
p=np.arange(0,0.51,0.01)
runge=1000000

sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])


x1=[]
x2=[]
x3=[]
y1=sx
y2=sy
y3=sz

for i in range(runge):
    l=ortho_group.rvs(3)
    x1.append(l[0][0]*sx+l[0][1]*sy+l[0][2]*sz)
    x2.append(l[1][0]*sx+l[1][1]*sy+l[1][2]*sz)
    x3.append(l[2][0]*sx+l[2][1]*sy+l[2][2]*sz)


x1=np.array(x1)
x2=np.array(x2)
x3=np.array(x3)


s11=np.kron(x1,y1)
s12=np.kron(x1,y2)
s13=np.kron(x1,y3)

s21=np.kron(x2,y1)
s22=np.kron(x2,y2)
s23=np.kron(x2,y3)

s31=np.kron(x3,y1)
s32=np.kron(x3,y2)
s33=np.kron(x3,y3)

t2=time.time()
print(t2-t1)

def fun(p,s11,s12,s13,s21,s22,s23,s31,s32,s33):   
    psi=np.array([np.sqrt(p),0,0,-np.sqrt((1-p))])
    #psi=(psi/np.linalg.norm(psi))

    E11=np.matmul(np.matmul(s11,psi),psi)
    E12=np.matmul(np.matmul(s12,psi),psi)
    E13=np.matmul(np.matmul(s13,psi),psi)

    E21=np.matmul(np.matmul(s21,psi),psi)
    E22=np.matmul(np.matmul(s22,psi),psi)
    E23=np.matmul(np.matmul(s23,psi),psi)

    E31=np.matmul(np.matmul(s31,psi),psi)
    E32=np.matmul(np.matmul(s32,psi),psi)
    E33=np.matmul(np.matmul(s33,psi),psi)

    a0=((abs(+E11+E12+E21-E22)))
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
c=[]
r=[]
for i in p:
    d=fun(i,s11,s12,s13,s21,s22,s23,s31,s32,s33)
    count=runge
    for k in d:
        if max(k)<2:
            count=count-1
    c.append(count/runge)
    r.append(runge)
    print(i,count/runge)

'''
df=pd.DataFrame({'P':p,'Prob':c,'No. Measure':r})

df.to_excel(r'output.xlsx')
'''