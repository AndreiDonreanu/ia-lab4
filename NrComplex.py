
class NrComplex:

    def __init__(self,a,b):
        self.a=a
        self.b=b


    def __str__(self):
        return "(%s"%self.a+","+"%s"%self.b+")"

    def __repr__(self):
        return "(%s"%self.a+","+"%s"%self.b+")"

    def __add__(self,other):
        return NrComplex(self.a+other.a,self.b+other.b)
    def __sub__(self,other):
        return NrComplex(self.a-other.a,self.b-other.b)

    def __mul__(self,other):
        return NrComplex(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
