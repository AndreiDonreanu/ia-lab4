from xml.etree.ElementTree import tostring


class Student:

    def __init__(self, name,grade):
        self.first_name = name
        self.grade = grade


    def __str__(self):
        return self.first_name+" "+"%s"%self.grade


    def __repr__(self):
        return self.first_name+" "+"%s"%self.grade

    def __eq__(self, other):
        return self.first_name==other.first_name


    def __lt__(self, other):
        return self.first_name<other.first_name

    def getsecondlowest(self,lista):
        rezultat=list()
        minim1=10
        minim2=11

        for i in lista:
            if i.grade<minim1:
                minim2=minim1
                minim1=i.grade

        for i in lista:
            if i.grade==minim2:
                rezultat.append(i)

        rezultat.sort()


        return rezultat