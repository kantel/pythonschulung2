class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, v):
        self.x += v.x
        self.y += v.y
    
    def print_vector(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

p1 = Vector(3, 4)
p2 = Vector(5.0, 7.3)
p1.add(p2)
p1.print_vector()
