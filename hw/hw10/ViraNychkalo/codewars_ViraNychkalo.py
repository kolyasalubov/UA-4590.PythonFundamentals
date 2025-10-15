####################################
class Ball():
    """
    Create a class Ball. 
    Ball objects should accept one argument for
    "ball type" when instantiated.
    If no arguments are given, ball objects should
    instantiate with a "ball type" of "regular."
    """
    def __init__(self, ball = "regular"):
        self.ball = ball 

# ball1 = Ball("super")
# ball2 = Ball()

# print(ball1.ball)
# print(ball2.ball)

########################################################3
import random
class Ghost():
    """
    Create a class Ghost
    Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of 
    "white" or "yellow" or "purple" or "red" when instantiated
    """
    def __init__(self): 
        self.color = random.choice(["white", "yellow", "purple", "red"])

# ghost1 = Ghost()
# ghost2 = Ghost()
# print(ghost1.color)
# print(ghost2.color)

############################################################################
class Human():
    """
    According to the creation myths of the Abrahamic religions, 
    Adam and Eve were the first Humans to wander the Earth.
    You have to do God's job. The creation method must return
    an array of length 2 containing objects (representing Adam and Eve).
    The first object in the array should be an instance of the class Man. 
    The second should be an instance of the class Woman. Both objects have
    to be subclasses of Human. Your job is to implement the Human, Man and Woman classes
    """
    @staticmethod
    def creation():
        return [Man(), Woman()]
class Man(Human):
    pass
class Woman(Human):
    pass

# people = Human.creation()
# print(type(Human.creation()[0])) 
# print(type(people[1])) 

#########################################################################
class Person:
    """
    Your task is to complete this Class, 
    the Person class has been created. 
    You must fill in the Constructor method to
    accept a name as string and an age as number, 
    complete the get Info property and getInfo 
    method/Info getter which should return
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def getInfo(self):
        return f"{self.name}'s age is {self.age}"

# person = Person("Vira", 18)
# print(person.getInfo()) 

#################################################################################
import math
class Sphere():
    """
    class Sphere.
    """
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
       V = round((4/3)*math.pi*(self.radius**3),5)
       return V
    
    def get_surface_area(self):
        A = round(4*math.pi*(self.radius**2),5)
        return A
    
    def get_density(self):
        density = self.mass/self.get_volume()
        return round(density, 5)
        
# ball = Sphere(2,50)
# print(ball.get_radius())  #2
# print(ball.get_mass()) #50
# print(ball.get_volume()) #33.51032
# print(ball.get_surface_area()) #50.26548
# print(ball.get_density()) #1.49208

############################################################################

    # I have a problem with the last(6) excersise, cause IDK how to do this for now, 
    # so maybe later i will return to this exersise, but now i'm doing pull request for
    # this project, cause i want you to check this work. Thank you:)

