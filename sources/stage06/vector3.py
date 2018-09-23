class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return(self)
    
    def __str__(self):
        return("(" + str(self.x) + ", " + str(self.y) + ")")

p1 = Vector(3, 4)
p2 = Vector(5.0, 7.3)
p3 = p1 + p2
print(p3)
print(type(p3))
