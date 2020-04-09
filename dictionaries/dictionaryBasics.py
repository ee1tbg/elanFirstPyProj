'''
Created on Jan 28, 2019

@author: Winterberger
'''
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2 ,"driveway": 1}

print(sensors)

'''
Items in dictionary are tied to their key (string or int). To add/change an object in a dict,
treat its key as its index
'''
animals_in_zoo={}
animals_in_zoo["zebras"]=8
animals_in_zoo['monkeys']=12
animals_in_zoo['dinosaurs']=0

print(animals_in_zoo)

'''
Update/add, multiple entries at once w update method
'''
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress":"Viola Davis","Best Picture": "Moonlight"})

'''
Dictionary comprehension
'''
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)

drinks_to_caffeine = {drinks:caffeine for drinks,caffeine in zipped_drinks}

'''
Basics test:
1. create dict comprehension of songs and playcounts
2. add a song
3. update playcount for a song by referencing its key
4. create new dictionary that is original dictionary and an empty one
'''
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {songs:playcounts for songs,playcounts in zip(songs,playcounts)}
print(plays)
plays["Purple Haze"]=1
#Listen to "Respect" 5 more times
plays.update({"Respect": plays["Respect"]+5})

library = {"The Best Songs":plays,"Sunday Feelings":{}}
print(library)