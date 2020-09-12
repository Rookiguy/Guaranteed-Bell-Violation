import numpy as np
from scipy.stats import ortho_group
import matplotlib.pyplot as plt
import time


runge=np.arange(0,1,0.01)
data=[]

sx=np.array([[0,1],[1,0]])
sy=np.array([[0,-1j],[1j,0]])
sz=np.array([[1,0],[0,-1]])

for p in runge:
    undata=[]
    for l in range(10000):
        bell=[]
        x=ortho_group.rvs(3)
        y=ortho_group.rvs(3)
        a1=x[0]
        a2=x[1]
        a3=x[2]
        b1=y[0]
        b2=y[1]
        b3=y[2]
        psi=np.array([1,p,p,1])
        psi=psi/(np.linalg.norm(psi))
        
        def d(a,b):
            s1=a[0]*sx+a[1]*sy+a[2]*sz
            s2=b[0]*sx+b[1]*sy+b[2]*sz
            s=np.kron(s1,s2)
            temp=np.matmul(psi,np.matmul(s,psi))
            return temp
    
        bell.append(abs(d(a1,b1)+d(a1,b2)+d(a2,b1)-d(a2,b2)))
        bell.append(abs(d(a1,b1)+d(a1,b2)-d(a2,b1)+d(a2,b2)))
        bell.append(abs(d(a1,b1)-d(a1,b2)+d(a2,b1)+d(a2,b2)))
        bell.append(abs(-d(a1,b1)+d(a1,b2)+d(a2,b1)+d(a2,b2)))

        bell.append(abs(+d(a1,b1)+d(a1,b3)+d(a2,b1)-d(a2,b3)))
        bell.append(abs(+d(a1,b1)+d(a1,b3)-d(a2,b1)+d(a2,b3)))
        bell.append(abs(+d(a1,b1)-d(a1,b3)+d(a2,b1)+d(a2,b3)))
        bell.append(abs(-d(a1,b1)+d(a1,b3)+d(a2,b1)+d(a2,b3)))

        bell.append(abs(+d(a1,b2)+d(a1,b3)+d(a2,b2)-d(a2,b3)))
        bell.append(abs(+d(a1,b2)+d(a1,b3)-d(a2,b2)+d(a2,b3)))
        bell.append(abs(+d(a1,b2)-d(a1,b3)+d(a2,b2)+d(a2,b3)))
        bell.append(abs(-d(a1,b2)+d(a1,b3)+d(a2,b2)+d(a2,b3)))

        bell.append(abs(+d(a1,b1)+d(a1,b2)+d(a3,b1)-d(a3,b2)))
        bell.append(abs(+d(a1,b1)+d(a1,b2)-d(a3,b1)+d(a3,b2)))
        bell.append(abs(+d(a1,b1)-d(a1,b2)+d(a3,b1)+d(a3,b2)))
        bell.append(abs(-d(a1,b1)+d(a1,b2)+d(a3,b1)+d(a3,b2)))

        bell.append(abs(+d(a1,b1)+d(a1,b3)+d(a3,b1)-d(a3,b3)))
        bell.append(abs(+d(a1,b1)+d(a1,b3)-d(a3,b1)+d(a3,b3)))
        bell.append(abs(+d(a1,b1)-d(a1,b3)+d(a3,b1)+d(a3,b3)))
        bell.append(abs(-d(a1,b1)+d(a1,b3)+d(a3,b1)+d(a3,b3)))

        bell.append(abs(+d(a1,b2)+d(a1,b3)+d(a3,b2)-d(a3,b3)))
        bell.append(abs(+d(a1,b2)+d(a1,b3)-d(a3,b2)+d(a3,b3)))
        bell.append(abs(+d(a1,b2)-d(a1,b3)+d(a3,b2)+d(a3,b3)))
        bell.append(abs(-d(a1,b2)+d(a1,b3)+d(a3,b2)+d(a3,b3)))

        bell.append(abs(+d(a2,b1)+d(a2,b2)+d(a3,b1)-d(a3,b2)))
        bell.append(abs(+d(a2,b1)+d(a2,b2)-d(a3,b1)+d(a3,b2)))
        bell.append(abs(+d(a2,b1)-d(a2,b2)+d(a3,b1)+d(a3,b2)))
        bell.append(abs(-d(a2,b1)+d(a2,b2)+d(a3,b1)+d(a3,b2)))

        bell.append(abs(+d(a2,b1)+d(a2,b3)+d(a3,b1)-d(a3,b3)))
        bell.append(abs(+d(a2,b1)+d(a2,b2)-d(a3,b1)+d(a3,b2)))
        bell.append(abs(+d(a2,b1)-d(a2,b2)+d(a3,b1)+d(a3,b2)))
        bell.append(abs(-d(a2,b1)+d(a2,b2)+d(a3,b1)+d(a3,b2)))

        bell.append(abs(+d(a2,b2)+d(a2,b3)+d(a3,b2)-d(a3,b3)))
        bell.append(abs(+d(a2,b2)+d(a2,b3)-d(a3,b2)+d(a3,b3)))
        bell.append(abs(+d(a2,b2)-d(a2,b3)+d(a3,b2)+d(a3,b3)))
        bell.append(abs(-d(a2,b2)+d(a2,b3)+d(a3,b2)+d(a3,b3)))
        
        t5=max(bell)
        undata.append(t5)
    undata=np.array(undata)
    data.append(np.mean(undata))
    
print(data)

plt.plot(runge,data)
plt.xlabel('P')
plt.ylabel('CHSH Value')
plt.legend()
plt.show()
            
