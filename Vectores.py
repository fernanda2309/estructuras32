import numpy as np 
import matplotlib.pylab as plt

lista =[25,12,15,66,12.55]

vector1= np.array(lista)
print(vector1)

vector2=np.array([12,14,16,18,20])
print(vector1+vector2)

vector3=np.array([2,3,4,5])
print(vector1+vector3)

vector4=np.array([2,3,4,5,6,7])
print(vector1+vector4)

x=np.linspace(-1,1,40)
y1=2*x
plt.figure(num='mi primer grafica')
plt.plot(x,y1)
