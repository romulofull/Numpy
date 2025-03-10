import numpy as np
a=np.array([1,2,3])
print(a)

b=np.array([[1,2],[3,4]])
print(b)

zeros =np.zeros(4)
print(zeros)
 
ones =np.ones(4)
print(ones) 

arange= np.arange(0,12,3)
print(arange)

lines =np.linspace(0,1,5)
print(lines)

eyes= np.eye(3)
print(eyes)

randoms= np.random.rand(2,5)
print(randoms)

a= np.array([1,2,3])
b= np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a*5)

a=np.array([1,2,3,4])
print(a[0])
print(a[-1])
print(a[2])
print(a[0:2])

b=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(b[0])
print(b[0][1])
print(b[0,1])
print(b[:1,1:3])
print(b[:2,1:3])

print(b.shape)
print(b.size)
print(b.dtype)
print(np.array([1,5,7], dtype='float'))
a= np.array([1,2,3,4,5,6])
print(a)
print(a.reshape((2,3)))

temperaturas=np.array([
    [15,18,20,22,19,17,16],
    [22,21,20,23,24,22,21],
     [12,14,16,13,11,12,14],
     [30,32,31,29,28,30,31],
])

print("Datos de Temperatuas son:")
print(temperaturas)
media=np.mean(temperaturas,axis=1)
print(media)
maxima=np.max(temperaturas,axis=1)
print(maxima)
minima=np.min(temperaturas, axis=1)
print(minima)
desviacion=np.std(temperaturas,axis=1)
print(desviacion)
uno=temperaturas+1
print(uno)
print(temperaturas[:,2])

tercerycuarto=temperaturas[0,2:4]=25
print(tercerycuarto)
print(temperaturas)

a= temperaturas.reshape((2,14))
print(a)
b= np.corrcoef(temperaturas)
print(b)


import matplotlib.pyplot as plt
estado = np.array(["desaprobados", "aprobados","promocionados"])
cantidad= np.array([2,10,7])
plt.bar(estado,cantidad)
plt.title('Cantidad de personas segun su estado')
plt.show()

plt.pie(cantidad, labels=estado)
plt.title('Cantidad de personas según su estado')
plt.show()

meses= np.array(["Enero","Febrero","Marzo","Abril"])
ventas= np.array ([1500, 2200, 1800, 2500])
plt.plot(meses,ventas)
plt.title('Ventas Mensuales')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.show()

notas= np.array([72,85,92,78,65,88,95,60,70,82,90,76,84,73,88,79,93,68,87,91])
plt.hist(notas, bins=10, edgecolor= 'black')
plt.title('Notas de exámenes')
plt.xlabel('Notas')
plt.ylabel('Frecuencia')
plt.show()