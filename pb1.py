import Student

s1=Student.Student("Andrei",8)
s3=Student.Student("Cristian",5)
s2=Student.Student("Mihai",5)
s4=Student.Student("Vidraru",3)

lista=[s1,s2,s3,s4]

rezultat=s1.getsecondlowest(lista)
print(lista)
print(rezultat)