'''
Created on Apr 8, 2019

@author: Winterberger
'''

'''
Create an exception class, use it
'''
# Define your exception up here:
class OutOfStock(Exception):
    print("Cant")

# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"
    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        else:
            self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

'''
Within a subclass, override a method defined in the parent class. This can define an Admin as a subclass of users for example
'''
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text
    
class User:
    def __init__(self, username):
        self.username = username
    
    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text
      
class Admin(User):
    def edit_message(self,message,new_text):
        message.text = new_text
        
        
'''
User super method to build on a superclass's methods:
use the constructor from PotatoSalad, but then add extra ingredients
'''
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40
        

'''
Define Interface (same method for different classes) to get the price of insurance for 'any' item
'''

class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return 0.001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return 0.00005 * self.price_of_insured_item
  
myHouse = HomeInsurance(100000)
myCar = VehicleInsurance(10000)
print("Home Insurance Rate is: {}".format(myHouse.get_rate()))
print("Car Insurance Rate is %0.2f " % myCar.get_rate())

'''
Polymorphism: same call (function, method, interface) does different things depending on the class its operating on.
In an intuitive way!
'''

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

'''
Define new method that mimics Python builtin to 'add' atoms to make a molecule
'''
class Atom:
    def __init__(self, label):
        self.label = label
  
    #represent Atom as a string
    def __repr__(self):
        return "{atomstr}".format(atomstr=self.label)
  
    #allow addition of atoms to create a molecule
    def __add__(self, other):
        return Molecule([self,other])
    
class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms
  
    #represent the molecule as the concatenation of its atoms
    #TODO allow detection of multiples of an atom, update name accordingly
    def __repr__(self):
        moleculestr = ""
        for i in self.atoms:
            moleculestr += str(i)
        return (moleculestr)
    
    #Allow 'addition' of molecules
    def __add__(self, other):
        return Molecule([self,other])
      
sodium = Atom("Na")
chlorine = Atom("Cl")

#define traditional method of creating salt
salt_ugly = Molecule([sodium.label, chlorine.label])

#use __add__ to create salt
salt_pretty = sodium + chlorine

#print lists of atoms in each type of molecule
print(salt_ugly.atoms)
print(salt_pretty.atoms)

#print Molecule names
print(salt_ugly)
print(salt_pretty)


'''
More examples - give a Class that we intend to use like a list (but with methods) some list characteristics
'''
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers
    
    def __len__(self):
        return len(self.lawyers)
  
    def __contains__(self,lawyer):
        return lawyer in self.lawyers
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

print(len(d_and_p))
print("Donelli" in d_and_p)
print("Alladin" in d_and_p)

'''
Final: sort a list when it's initialized and when it's appended to
'''
class SortedList(list):
  
    def __init__(self, *args):
        list.__init__(self,*args)
        print("preinitsort")
        print(self)
        self.sort()
        print("self from init:")
        print(self)
    
    def append(self, value):
        print("SELF")
        print(self)
        print(value)
        super().append(value)
        self.sort()
    
myList = SortedList([2,1])
print("myList")
print(myList)
myList.append(3)
print(myList)
