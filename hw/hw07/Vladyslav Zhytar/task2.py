#10.2(second)

class Human:
    
    def __init__(self,name):
        self.name=name

    def welcome(self):
        return f"Hello {self.name}"
    
    @classmethod
    def species(cls):
        return "Your species Homosapiens"
    
    @staticmethod
    def static():
        return "Have a nice day"
    

human=Human("Vlad")
print(human.welcome())
print(Human.species())
print(human.static())
