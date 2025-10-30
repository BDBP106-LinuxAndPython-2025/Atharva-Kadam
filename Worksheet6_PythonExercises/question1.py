"""(1) Define a class called ’Car’. The class intance should take
required arguments as make,model, year and color. Define default values
 of ’False’ for the attributes called ’started’,0 for the
 attribute ’speed’, and ’200’ as the maximum speed. There should be a total of
7 attributes in the __init__ function.
(a) Create an instance of the above class called toyota_camry with arguments of car
make as ’Toyota’, model as ’Camry’, year as ’2022’ and color ’Red’. Print the values of
these attributes using the instance you just created."""
import functools


class Car:
    showroom="NewAge"
    def __init__(self, make, model, year, color,started=False,speed=0,maximum_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color=color
        self.started = started
        self.speed = speed
        self.maximum_speed = maximum_speed

    """(e) Now define a class attribute called showroom with value NewAge. Also define a func-
        tion with decorator @classmethod that changes this value upon user request. Again
        print the value of __dict__ attribute, what is the output? Describe the output."""

    @classmethod
    def showroom_change(cls,show_room_name):
        cls.showroom=show_room_name


    #g sub question:
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color}"


    @staticmethod
    def show_intro_message():
        print("Class: Car  and the attributes of the class")



#the output shows a new key value pair showing showroom_change.
print(Car.__dict__)

toyota_camry=Car("Toyota", "Camry", 2022, "Red")
print(toyota_camry.make,toyota_camry.model,toyota_camry.year,toyota_camry.color)



"""(b) Create another instance of this class called ’ford mustang’ with make as ”Ford”,
model as ”Mustang”, year 2022 and color ’Black’.Print all the 7 attributes for this in-
stance."""
ford_mustang=Car("Ford","Mustang",2022,"Black")
print(ford_mustang.make,ford_mustang.model,ford_mustang.year,ford_mustang.color)



"""(c) How can you be sure that the above attributes belong to the instance and not the
class? Try typing print(Car.make). Do you get an error, and if so what error do you
get? How will you fix this error in your main program?"""
# print(Car.make)
#it gives attribute error
#Traceback (most recent call last):
#   File "C:\WorkSheet6-Python_Excercises\question1.py", line 35, in <module>
#     print(Car.make)
#           ^^^^^^^^
# AttributeError: type object 'Car' has no attribute 'make'


#to correct it:
print(ford_mustang.make)



"""(d) Execute the command print(Car.__dict__). Describe the output. The __dict__
attribute holds a dictionary containing the writable members of the underlying class or
instance. Each key value represents an attribute or method name. When you access a
class member through the class object, Python automatically searches for the member’s
name in the __dict. If the name isn’t there, you get an AttributeError."""

print(Car.__dict__)



"""(f) Print the value of toyota_camry.__dict__. How is this output different from
Car.__dict__? Explain."""
print(toyota_camry.__dict__)
print(Car.__dict__)

#toyota_camry.__dict__ gives the attributes of the instance.
#while Car.__dict__ gives the attributes of the whole class.




"""(g) Python also supports what are called magic methods or dunder (double underscore)
methods that are called automatically in response to specific operations. For example, de-
fine a function as below. and execute the statement print(str(<name-of_class)). Test
this with the above two class instances you created. For example str(toyota_camry).
What is the output? There are other magic methods such as ___iter__, __repr__ etc."""
print(str(Car))
print(str(toyota_camry))
print(str(ford_mustang))#The output we are getting is that we are getting the string representation of the instances




"""(h) Define a static method called show_intro_message that prints the purpose of this
class.
def __str__(self):
return f"{self.make} {self.model} {self.color| ({self.year})"""
Car.show_intro_message()