'''
Created on Jan 29, 2019

@author: Winterberger
'''
from tkinter.scrolledtext import example

'''
Avoid exception if key doesn't exist
'''
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")

'''
Get values properly, and identify default value if they don't exist
'''
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder',100000)
print(tc_id)
stack_id = user_ids.get('superStackSmash',100000)
print(stack_id)

'''
Use pop method to call items by key and simultaneously remove them from the dictionary.
'''
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains",0)
health_points += available_items.pop("power stew",0) + available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

'''
use .keys and .values methods to VIEW keys/values in dictionary. Need secondary action to make them actionable.
'''
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for i in num_exercises.values():
    total_exercises += i
print(num_exercises.keys())
print(total_exercises)

'''
Or get all items in (key,item/s) sets via .items
'''
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation,number in pct_women_in_occupation.items():
    print('Women make up {} percent of {}s'.format(number,occupation))
    

'''
Final exam
'''
tarot = { 1:    "The Magician", 2:    "The High Priestess", 3:    "The Empress", 4:    "The Emperor", 5:    "The Hierophant", 6:    "The Lovers", 7:    "The Chariot", 8:    "Strength", 9:    "The Hermit", 10:    "Wheel of Fortune", 11:    "Justice", 12:    "The Hanged Man", 13:    "Death", 14:    "Temperance", 15:    "The Devil", 16:    "The Tower", 17:    "The Star", 18:    "The Moon", 19:    "The Sun", 20:    "Judgement", 21:    "The World", 22: "The Fool"}
spread = {}
#spread['past']=tarot.pop(13)
spread.update({'past': tarot.pop(13), 'present': tarot.pop(22), 'future': tarot.pop(10)})

for i,j in spread.items():
    print('Your {} is the {} card.'.format(i,j))
    
