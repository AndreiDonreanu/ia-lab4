
from Vector import Vector

v1=Vector(1,5,6)
v2=Vector(8,1,2)

print("v1+v2="+"%s"%(v1+v2))
print("v1-v2="+"%s"%(v1-v2))

print("dot product="+"%s"%(v1.dot_product(v2)))
print("cross product="+"%s"%(v1.cross_product(v2)))