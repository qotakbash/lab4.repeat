from math import pi
default_radius =5
def circle_area(r = default_radius):
    return (pi*(r**2))
def circle_perimeter(r = default_radius):
    return 2*pi*r

default_a =15
def square_area(a =default_a):
    return a*a
def square_perimeter(a = default_a):
    return 4*a


from math import sqrt
a=7
b=2
c=8
def triangle_perimeter(a=a, b=b, c=c):
    return a+b+c
def triangle_area(a=a, b=b, c=c):
    return sqrt(4*a**2*b**2 -(a**2+b**2-c**2)*2)/4


    test.py
from figures.circle.code import *
from figures.triangle.code import *
from figures.square.code import *

from figures import circle_area,square_perimeter,triangle_area

print(f"the area of the circle is : {circle_area()} ")

print(f"the perimeter of the square is : {square_perimeter(10)}")

print(f"the area of the triangle is : {triangle_area()}")