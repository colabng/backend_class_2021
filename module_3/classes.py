"""Python is a multi-paradigm programming language. It supports different programming approaches.
One of these approaches is OOP (Object Oriented Programming)
An object has two characteristics:
    - attributes (variables)
    - behavior (functions)

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY 
(Don't Repeat Yourself).

Class
A class is a blueprint for the object.

__init__ : It is the initializer method that is first run as soon as the object is created.

Methods
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

Inheritance
Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
The newly formed class is a derived class (or child class).
"""

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

print(blu.dance())