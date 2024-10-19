from math import sqrt

trace=[("UP",5),("DOWN",3),("LEFT",3),("RIGHT",2)]

dirx=0
diry=0

for i in trace:
    if i[0]=="UP":
        diry+=i[1]

    if i[0]=="DOWN":
        diry-=i[1]

    if i[0]=="LEFT":
        dirx-=i[1]
    if i[0]=="RIGHT":
        dirx+=i[1]

print(round(sqrt(dirx**2+diry**2)))