"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."


print ("Mad Libs has started...")
name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter a 2nd adjective: ")
adj3 = input("Enter a 3rd adjective: ")
verb = input("Enter a verb: ")
nou1 = input("Enter a noun: ")
nou2 = input("Enter 2nd noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")



print ("This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." % (name, adj1, adj2, animal, food, verb, nou1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, nou2))
