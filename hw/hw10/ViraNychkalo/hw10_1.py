##################TASK1#######################3
class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def display_info(self):
        return f"Polygon sides - {self.sides}"
        
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
# r = Rectangle(10, 5)
# print(r.display_info()) 
# print(f"Area: {r.area()}")  


################TASK2#################
class Human():
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f"Hello {self.name}!"
    
    @classmethod
    def message_homosapiens(cls):
        return "Species: Homosapiens"
    @staticmethod
    def message_my():
        return "Всі ми люди і всі ми робимо помилки, головне - те, як ми діємо далі."

# h = Human("Vira")
# print(h.greeting())            
# print(Human.message_homosapiens())  
# print(Human.message_my())     

####################TASK3#########################
class Employee():
    """
    This is an Employee class
    """
    counter = 0 
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        Employee.counter += 1

    def number_of_employees(self):
        print(f"In this company we have {Employee.counter} workers.")

    def display(self):
        print(f"{self.name}'s salary - {self.salary}")
                             # for me
print(Employee.__base__)     # <class 'object'>
print(Employee.__dict__)     # словник атрибутів класу
print(Employee.__name__)     # 'Employee'
print(Employee.__module__)   # '__main__'
print(Employee.__doc__)      # This is an Employee class

# e1 = Employee("Vira", 50000)
# e2 = Employee("Oleh", 10000)

# e1.display()  
# e2.display() 
# e1.number_of_employees() 







