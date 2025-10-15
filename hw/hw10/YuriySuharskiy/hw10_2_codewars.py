# I
class Ball():
    def __init__ (self, ball_type = "regular"):
        self.ball_type = ball_type

# II
import random

class Ghost():
    color=["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(Ghost.color)

# III
class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    human1 = Man()
    human2= Woman()
    return[human1,human2]

# IV
class Person():
    def __init__(self, name:str,age:int):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"

# V
from math import pi

class Sphere():
    def __init__ (self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
        
    def get_mass(self):
        return self.mass
        
    def get_volume(self):
        return round(4/3*pi*self.radius**3, 5)
        
    def get_surface_area(self):
        return round(4*pi*self.radius**2, 5)
        
    def get_density(self):
        return round(self.mass/self.get_volume(), 5)
    
# VI
import re

def class_name_changer(cls, new_name):
    pattern = r'^[A-Z][a-zA-Z0-9]+$'
    if re.match(pattern, new_name) and new_name:
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name")