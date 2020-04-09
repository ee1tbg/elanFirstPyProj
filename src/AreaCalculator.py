'''
Created on Nov 10, 2018

@author: Winterberger
'''
from math import *
def CalculateArea(shape):
    area = 0.
    ##radius = 0.
    ##base = 0.
    ##height = 0.
    
    print (shape.lower())
    
    if shape.lower() == "circle":
        radius = float(input("Radius (in inches): "))
        area = pi * radius**2.
    else:
        base = float(input("Base (in inches): "))
        height = float(input("Height (in inches): "))
        area = base * height
    
    if shape.lower() == "square" and base != height:
        print ("That's not a sqaure but ok.")
    if shape.lower() == "triangle":
            area *= 0.5
            
    return area
valid_shape_1 = "Circle"
valid_shape_2 = "Square"
valid_shape_3 = "Rectangle"
valid_shape_4 = "Triangle"
valid_shape_5 = "Exit"
test_input = (input("Please input the shape whose area you want to calculate. \n Valid shapes are %s, %s, %s, %s \n To exit type %s \n Shape:" % (valid_shape_1, valid_shape_2, valid_shape_3, valid_shape_4, valid_shape_5)))
while (test_input.lower() != "exit"):
    result = print("\n The area of your " + test_input + " is " + str(CalculateArea(test_input)) + ".\n")
    test_input = (input("Next shape: (To exit type %s) \n Shape:" % (valid_shape_5)))
    
##result = print(CalculateArea(test_input))