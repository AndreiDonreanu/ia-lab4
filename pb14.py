import numpy
from math import sqrt

# Open the file and read data
f = open("vectors.txt.txt", 'r')
g = f.readline().strip()  # Number of vectors
dictionar = dict()


miux = 0
miuy = 0
miuz = 0

listux = []
listuy = []
listuz = []


for i in range(int(g)):
    h = f.readline().strip()
    l = h.split()
    tupla = (int(l[0]), int(l[1]), int(l[2]))
    dictionar.setdefault(i, tupla)


for i in range(int(g)):
    tupla = dictionar.get(i)
    listux.append(tupla[0])
    listuy.append(tupla[1])
    listuz.append(tupla[2])

miux = sum(listux) / int(g)
miuy = sum(listuy) / int(g)
miuz = sum(listuz) / int(g)


print(f"Mean of x, y, z are: ({miux:.2f}, {miuy:.2f}, {miuz:.2f})")
print(f"NumPy calculated mean: ({numpy.mean(listux):.2f}, {numpy.mean(listuy):.2f}, {numpy.mean(listuz):.2f})")


sqx = [(x - miux) ** 2 for x in listux]
sqy = [(y - miuy) ** 2 for y in listuy]
sqz = [(z - miuz) ** 2 for z in listuz]

varx = sum(sqx) / len(listux)
vary = sum(sqy) / len(listuy)
varz = sum(sqz) / len(listuz)


deltax = sqrt(varx)
deltay = sqrt(vary)
deltaz = sqrt(varz)


print(f"Standard deviation (manual): ({deltax:.2f}, {deltay:.2f}, {deltaz:.2f})")
print(f"NumPy calculated std: ({numpy.std(listux):.2f}, {numpy.std(listuy):.2f}, {numpy.std(listuz):.2f})")
