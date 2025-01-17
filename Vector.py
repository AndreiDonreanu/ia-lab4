class Vector:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(%s,%s,%s)"%(self.x,self.y,self.z)
    def __repr__(self):
        return "(%s,%s,%s)"%(self.x,self.y,self.z)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)