# 1 version ________________________________
class Polygon():
    def __init__(self, *args):
        self.sides = []
        for i in args:
            self.sides.append(i)

class Rectangle(Polygon):

    def area(self):
        return self.sides[0]*self.sides[1]
        

a = Rectangle(3,4,3,4)

print(a.area())

# 2 version ___________________________
class Polygon():
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter {str(i+1)} side: ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)

    def area(self):
        a, b = self.sides
        area = a * b
        return area
    
rec = Rectangle()

rec.input_sides()

print(rec.area())