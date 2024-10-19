from GeometricForm import GeometricForm
from math import  pi

class Circle(GeometricForm):

    def __init__(self,raza):
        super().__init__()
        self.raza = raza

    def getArea(self):
        return self.raza*self.raza*pi

    def getPerimeter(self):
        return 2*self.raza*pi

