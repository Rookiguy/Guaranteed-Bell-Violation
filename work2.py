from scipy.stats import ortho_group
import numpy as np
import matplotlib.pyplot as plt

data=[]
prob=[]

for l in range(1000000):
    x=ortho_group.rvs(3)
    y=ortho_group.rvs(3)
    z=ortho_group.rvs(3)
    bell=[]

    a1=x[0]
    a2=x[1]
    a3=x[2]

    b1=y[0]
    b2=y[1]
    b3=y[2]

    def d(x,y):
        return -np.dot(x,y)

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

    for i in bell:
        if i>2:
            t5=max(bell)
    
    data.append(round(t5,2))

data.sort()

mata=data

file1=open('test.xls','w')
file1.write(str(data))
file1.close()

for i in mata:
    temp=mata.count(i)
    if temp>1:
        for j in range(temp-1):
            mata.remove(i)
    prob.append(temp)

print('Organized Data is',mata)
print('\n\n\n')
print('Prob dist is',prob)
print('\n\n\n')

sum=0
for i in prob:
    sum=sum+i

mata=np.array(mata)
prob=np.array(prob)
norm_prob=prob/sum
print('sum is ', sum)
print('normalized prob dist is',norm_prob)

plt.plot(mata,norm_prob)
plt.xlabel('CHSH')
plt.ylabel('Frequency')
plt.show()
