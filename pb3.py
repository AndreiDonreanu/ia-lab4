def hasSame3elements(v1,v2):

    set1=set()
    set2=set()
    l1=len(v1)-2
    l2=len(v2)-2


    for i in range(l1):
        rez1=(v1[i],v1[i+1],v1[i+2])
        set1.add(rez1)

    for i in range(l2):
        rez2=(v2[i],v2[i+1],v2[i+2])
        set2.add(rez2)






    return not set1.isdisjoint(set2)


v1=[1,10,9,10,8]
v2=[8,10,9,7,6]
v3=[10,9,10,7,6]

print(hasSame3elements(v1,v2))
print(hasSame3elements(v1,v3))