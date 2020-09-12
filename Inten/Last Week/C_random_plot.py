import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.stats import ortho_group
from random import *



def random_three_vector():
  u = random()
  v = random()
  theta = 2 * np.pi * u
  phi = np.arccos(2*v-1)
  x   = np.sin(theta)*np.cos(phi)
  y   = np.sin(theta)*np.sin(phi)
  z   = np.cos(theta)
  return [x,y,z]

trials=1000000

a=[]
b=[]
c=[]
for i in range(trials):
  temp=random_three_vector()
  a.append(temp[0])
  b.append(temp[1])
  c.append(temp[2])
  

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(a, b, c, c='r', marker='.')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()