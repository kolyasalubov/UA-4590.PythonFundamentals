#10.2 (first)

class Polygon:

    def __init__(self,n):
        self.n=n
        self.sides=[]
    
    def enter_sides(self):
        for item in range(self.n):
            self.sides.append((input(f" Enter {item+1} side: ")))

    def __str__(self):
        return f" The polygon has {self.n} sides: {self.sides}"
    
    def find_area(self):
        pass 


class Rectangle(Polygon):

    def __init__(self):
        super().__init__(4)

    def enter_sides(self):
        return super().enter_sides()
    
    def find_area(self):
        return float(self.sides[0])*float(self.sides[1])
    
    def __str__(self):
        return super().__str__()
    
    
rectangle=Rectangle()
rectangle.enter_sides()
print(rectangle)
print(f' The area of rectangle is {rectangle.find_area()}')