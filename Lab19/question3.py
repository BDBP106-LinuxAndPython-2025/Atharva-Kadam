# (3) Write a program to convert a tuple of angles into a list of tuples with each tuple containing
# the sine and cosine of an angle
import math
def convert_angles(a):
    l=[]
    for i in range(len(a)):
        rad_i=a[i] * (math.pi/180)
        sin_i= math.sin(rad_i)
        cos_i=math.cos(rad_i)
        tup=(sin_i,cos_i)
        l.append(tup)
    return l
angle_tuple=tuple(map(int,input("Enter the angles:").split(",")))
print(angle_tuple)
list_of_sin_cosine=convert_angles(angle_tuple)
print(list_of_sin_cosine)


