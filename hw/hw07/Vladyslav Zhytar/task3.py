#10.2(third)

class Employee:

    """
    This class is intended for counting employees
    """

    total=0

    def __init__(self,name,salary):
        Employee.total+=1
        self.name=name
        self.salary=salary
        
    @classmethod
    def print_total(cls):
        return f" Only {cls.total} employees"
    
    def __str__(self):
        return f" Employee {self.name} has {self.salary} $ in month"
    

emp1=Employee("Vlad",1200)
emp2=Employee("Anrew",2800)
emp3=Employee("Max",800)
print(Employee.print_total())
print(emp2)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)