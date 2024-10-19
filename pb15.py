import random
from zoneinfo import reset_tzpath


def Monte_Carlo_PI(num_points,raza):
    in_cerc=0
    for i in range(num_points):
        x=random.uniform(-raza,raza)
        y=random.uniform(-raza,raza)
        if x**2+y**2<=raza**2:
            in_cerc+=1


    return 4*(in_cerc/num_points)


num_points=1000000
raza=1
print("O estimare a lui pi este:"+"%s"%Monte_Carlo_PI(num_points,raza))