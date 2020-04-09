'''
Created on Mar 9, 2019

@author: Winterberger
'''

'''
Create Class with method that just prints something
'''
class Rules:
    def washing_brushes(self):
        return ("Point bristles towards the basin while washing your brushes.")
    
'''
Define Class Circle with a method that calculates the area of a circle based on the radius
Then instantiate that class Circle as an object 'circle'
Then calculate the areas of a few circles using the Circle.area method on object circle
'''
class Circle:
    pi = 3.14
    def area(self,radius):
        return self.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)


'''
Define Circle class. It takes in a diameter and returns the area (for now). Define constructor (__init__) that prints out the passed-in diameter
'''
class Circle2:
    pi = 3.14
    
    # Add constructor here:
    def __init__(self,diameter):
        print("New circle with diameter: {}".format(diameter))
        
    def area(self,diameter):
        return self.pi * (diameter / 2) ** 2
    
teaching_table = Circle2(36)

'''
Iterate though list of items, return the number of 's' in an element if that element has attribute 'count'
'''
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for index in how_many_s:
    if hasattr(index, "count"):
        scount = 0
        for items in range(len(index)):
            scount += int(index[items] == 's')
        print (scount)

'''
Add circumference method to Circle class
'''
class Circle3:
    pi = 3.14
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2
    def circumference(self):
        return 2 * self.pi * self.radius
    
medium_pizza = Circle3(12)
teaching_table = Circle3(36)
round_room = Circle3(11460)

print (medium_pizza.circumference())
print (teaching_table.circumference())
print (round_room.circumference())

'''
Print directories of objects
'''
print(dir(5))
def this_function_is_an_object(nothing):
    return nothing
print("\n")
print(dir(this_function_is_an_object))

'''
Add string representation dunder (double underscore) to help debug
'''
class Circle4:
    pi = 3.14
    
    def __init__(self, diameter):
        self.radius = diameter / 2
    
    def __repr__(self):
        return "Circle with radius {}".format(self.radius)
    
    def area(self):
        return self.pi * self.radius ** 2
    
    def circumference(self):
        return self.pi * 2 * self.radius
  
  
medium_pizza = Circle4(12)
teaching_table = Circle4(36)
round_room = Circle4(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

"""
Final test.
"""
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    #Add a passed-in grade to the student's list of grades  
    def add_grade(self,grade):
        if type(grade) == Grade:
            self.grades.append(grade.mathable_score())

    #Determine a student's average - not maintained
    def get_average(self):
        #print(sum(self.grades))
        return sum(self.grades)/len(self.grades)

class Grade:
    minimum_passing = 65

    #initialize the class to include a score
    def __init__(self, score):
        self.score = score

    #include a method that returns an int of the score, so you can actually use it
    def mathable_score(self):
        return int(self.score)

    def is_passing(self):
        return self.score > self.minimum_passing

#define students and their years(not used yet)
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#define Grades, which seems inefficient..
perfect_score = Grade(100)
half_score = Grade(50)
no_score = Grade(0)

print(perfect_score.is_passing())

#Add scores for pieter and roger
pieter.add_grade(perfect_score)
roger.add_grade(perfect_score)
pieter.add_grade(half_score)
roger.add_grade(no_score)

#Determine if a student's average score is passing
print(Grade(pieter.get_average()).is_passing())
print(Grade(roger.get_average()).is_passing())