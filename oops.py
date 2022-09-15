##############################################################################################################################
""" Inheritance

When we create classes we can inherit methods and attributes from other already existing classes. This allows us to create a variety of different sub-classes or child classes based off of what is known as a parent class or super class.

"""
##############################################################################################################################

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'I am {self.name}. I am {self.age} years old.')

    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'dog'



# dazy = Dog('dazy', 5)

# dazy.speak()
# print(dazy.type)


##############################################################################################################################
# Overriding
"""Sometimes when we inherit from a parent class we want to have methods or attributes that have the same name as a method in the parent class but that have a different functionality. If we create a method or attribute inside of our child class with the same name as one in the parent it will override the parent class."""
##############################################################################################################################

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'I am {self.name}. I am {self.age} years old.')

    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'dog'

    def speak(self):
        print('I am a dog')
        # super().speak()



dazy = Dog('dazy', 5)

# dazy.speak()
# print(dazy.type)


##############################################################################################################################
# Method Overloading
""" There are only certain methods which can be overloaded
like __add__, __sub__, __mul__, __gt__, __ge__, __lt__, __le__ and many more.
"""
##############################################################################################################################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = (self.x, self.y)

    def __add__(self, other):
        print(self)
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


p1 = Point(5,40)
p2 = Point(1,1)

# p3 = p1 + p2
# print(p3)

##############################################################################################################################

##############################################################################################################################
