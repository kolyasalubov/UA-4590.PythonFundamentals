#1
# class Ball(object):
    
#     def __init__(self, ball_type="regular"):
#         self.ball_type=ball_type

#2
# import random
# class Ghost(object):
    
#     def __init__(self,color=None):
#         self.color=color if color else random.choice(["white","red","purple","yellow"])

#3
# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# Eva=Woman()
# Adam=Man()

# def God():
#     return [Adam,Eva]

#4
# class Person:

#     def __init__(self,name:str,age:int):
#         self.name=name
#         self.age=age
    
#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"

#5
# from math import pi
# class Sphere(object):
    
#     def __init__(self,radius:float,mass:float):
#         self.radius=radius
#         self.mass=mass

#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         return round(((4/3)*pi*self.radius**3),5)
    
#     def get_surface_area(self):
#         return round((4*pi*self.radius**2),5)
    
#     def get_density(self):
#         return round((self.mass/self.get_volume()),5)

#6
# def class_name_changer(cls, new_name):
#     if new_name[0].isupper() and new_name.isalnum():
#         cls.__name__=new_name
#     else:
#         raise ValueError
