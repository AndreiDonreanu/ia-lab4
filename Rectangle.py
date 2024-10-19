from GeometricForm import GeometricForm


class Rectangle(GeometricForm):

    def __init__(self,lungime,latime):
        super().__init__()
        self.lungime = lungime
        self.latime = latime

    def getArea(self):
        return self.latime * self.lungime

    def getPerimeter(self):
        return (self.lungime + self.latime)*2

