class Employee():
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def number_of_employees(cls):
        return cls.count
    
    def employee_info(self):
        print(f"Employee {self.name} has a salary of {self.salary} UAH")
    
emp1 = Employee("Yuriy", 1000)
emp2 = Employee("Julia", 2000)

print(emp1.number_of_employees())
print(Employee.number_of_employees())
emp1.employee_info()
emp2.employee_info()

print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)