# Complete your power function here
from tkinter import N


def power(n):
    return lambda a:a**n
 
 
# You are not allowed to modify the following codes
square = power(2)
cube = power(3)
n = int(input("Please input an integer: "))
print ("Square of",n,"is",square(n))
print ("Cube of",n,"is",cube(n))
