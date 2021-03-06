'''
Created on Jun 6, 2019

@author: Winterberger
'''
class Menu:
    def __init__(self, name, items, start_time, end_time):
        '''
        print(name + " is served from %d to %d." % (start_time, end_time))
        '''
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
      
    def __repr__(self):
        return (self.name + " menu available from %d to %d." % (self.start_time, self.end_time))
    
    def calculate_bill(self, purchased_items):
        bill = 0.
        for item in purchased_items:
            bill += self.items[item]
        print('This ' + self.name + ' bill comes to $%0.2f.' % bill)
        return bill
    
  
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)

early_bird = Menu("Early-Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)

kids = Menu("Kids Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

print (brunch)
print (early_bird)
print (dinner)
print (kids)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])