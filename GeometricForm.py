from abc import abstractmethod


class GeometricForm:

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass
