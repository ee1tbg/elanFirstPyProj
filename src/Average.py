'''
Created on Nov 10, 2018

@author: Winterberger
'''
##from math import 
def average(*args):
    num = sum(args)
    print(num)
    den = len(args)
    print (den)
    average = float(num/den)
    return average


Argument = []
i = 0
print(Argument[i])
while (Argument[i] >= 0):
    Argument[i] = input("Input next value to take average of: ")
    i += 1

print(average(Argument))