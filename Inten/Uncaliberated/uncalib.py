import numpy as np
from itertools import combinations as cmb
import matplotlib.pyplot as plt
from scipy.stats import ortho_group
from numba import jit, prange
import time

start_time=time.time()

rnge=100000
@jit
def random_three_vector():

    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return [x,y,z]

@jit
def norm(a):
   return np.sqrt(np.dot(a,a))
@jit
def d(x,y):
   return -np.dot(x,y)
@jit
def f1(u,v,x,y):
   return abs(d(u,x)+d(u,y)+d(v,x)-d(v,y))
@jit
def f2(u,v,x,y):
   return abs(d(u,x)+d(u,y)-d(v,x)+d(v,y))
@jit
def f3(u,v,x,y):
   return abs(d(u,x)-d(u,y)+d(v,x)+d(v,y))
@jit
def f4(u,v,x,y):
   return abs(-d(u,x)+d(u,y)+d(v,x)+d(v,y))

      

@jit
def bfn(m):
   un_data=[]
   for l in prange(rnge):
      m1=[]
      m2=[]
      for o in prange(m):
         m1.append(random_three_vector())
      for p in prange(m):
         m2.append(random_three_vector())
      

      ar1=list(cmb(m1,2))
      ar2=list(cmb(m2,2))
      ar1=np.array(ar1)
      ar2=np.array(ar2)
      bell=[]

      for i in prange(len(ar1)):
         u=ar1[i][0]
         v=ar1[i][1]
         for j in prange(len(ar2)):
               x=ar2[j][0]
               y=ar2[j][1]
               bell.append(f1(u,v,x,y))

      for i in prange(len(ar1)):
         u=ar1[i][0]
         v=ar1[i][1]
         for j in prange(len(ar2)):
               x=ar2[j][0]
               y=ar2[j][1]
               bell.append(f2(u,v,x,y))
      
      for i in prange(len(ar1)):
         u=ar1[i][0]
         v=ar1[i][1]
         for j in prange(len(ar2)):
               x=ar2[j][0]
               y=ar2[j][1]
               bell.append(f3(u,v,x,y))

      for i in prange(len(ar1)):
         u=ar1[i][0]
         v=ar1[i][1]
         for j in prange(len(ar2)):
            x=ar2[j][0]
            y=ar2[j][1]
            bell.append(f4(u,v,x,y))

      t5=max(bell)
      un_data.append(round(t5,2))

   un_data.sort()
   mata=un_data
   un_data=np.array(mata)
   return un_data


def vis(m):
   mata=bfn(m)
   V=np.arange(0.7,1,0.01)     
   vy=[]

   for i in V:
      un_data=np.array(mata)
      un_data=i*un_data
      count=0
      for j in un_data:
         if j>2:
               count=count+1
      vy.append(count)

   vy=np.array(vy)
   count=0
   for i in vy:
      count=count+i
   print(count)
   vy=vy/rnge
   return vy

V=np.arange(0.7,1,0.01)

v2=vis(2)
v3=vis(3)
v4=vis(4)
v5=vis(5)
v6=vis(6)
v7=vis(7)
v8=vis(8)

stop_time=time.time()

print('Time taken is =',stop_time-start_time)
plt.plot(V,v2,label='m=2')
plt.plot(V,v3,label='m=3')
plt.plot(V,v4,label='m=4')
plt.plot(V,v5,label='m=5')
plt.plot(V,v6,label='m=6')
plt.plot(V,v7,label='m=7')
plt.plot(V,v8,label='m=8')
plt.xlabel('V')
plt.ylabel('Probability of violation')
plt.legend()
plt.show()
