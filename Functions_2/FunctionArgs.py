'''
Use special python None (immutable, falsy, unique value) to determine if we do something
'''

from review_lib import get_next_review, submit_review

# define review here!
review = get_next_review()

if review is not None:
    submit_review(review)

'''
Common functions that do something but don't return anything: subroutines
'''
# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)


'''
Set parameter to default value if no argument is passed in
'''

import os

def make_folders(folders_list, nest=False):
    if nest:
        """
        Nest all the folders, like
        ./Music/fun/parliament
        """
        path_to_new_folder = ""
        for folder in folders_list:
            path_to_new_folder += "/{}".format(folder)
            try:
                os.makedirs(path_to_new_folder)
            except FileExistsError:
                continue
    else:
        """
        Makes all different folders, like
        ./Music/ ./fun/ and ./parliament/
        """
        for folder in folders_list:
            try:
                os.makedirs(folder)

            except FileExistsError:
                continue

make_folders(['./Music', './fun', './parliament'])

'''
NOTE PARAMETERS WITH DEFAULT ARGUMENTS MUST COME AFTER ALL NON-DEFAULT PARAMETERS (otherwise how do you know if it's a default value or a different parameter)
'''

'''
Keyword arguments allow arguments to be specified at-will, and in any order
'''
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
    shape = shapes.draw_shape(shape_name, character)
    if not line_breaks:
        print(shape[1:-1])
    else:
        print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character="m", line_breaks = False)

'''
For mutable parameters (like a list), use None as a 'sentinal' or Flag
to instantiate the mutable parameter to the default value as the first step of the function
rather than within the function call
'''

def update_order(new_item, current_order=None):
    if current_order == None: 
        current_order = []
    current_order.append(new_item)
    return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)

'''
Unpack multiple returns (which are returned as a tuple;
an immutible set of values, which can be referenced individually by index into the tuple)
'''

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("hI")
print(the_scream)
print(the_whisper)

'''
Positional / variable # of arguments
'''

from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
    sentence = ""
    for arg in args:
        sentence += arg
    return sentence

print(myjoin(path_segment_1, path_segment_2, path_segment_3))

'''
Keyword arguments: kwargs
'''
# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(name="Tim", feeling="10/10",))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
    Baseball='3',
    Shirt='14',
    Guitar='70')

'''
Use all types of function parameters, in their necessary orders
'''
def main(filename, *args, user_list=None, **kwargs):
    if user_list is None:
        user_list = []

    if '-a' in args:
        user_list = all_users()

    if kwargs.get('active'):
        user_list = [user for user_list if user.active]

    with open(filename) as user_file:
        user_file.write(user_list)

'''
Act on unpacked positional and keyword arguments appropriately:
1. *args as a list
2. **kwargs as a dict
'''
def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
    for arg in args:
        text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

'''
'Pack' sets of information to fit 'unpacked' parameter types of unpacked positional/keyword arguments.
'''
from products import create_product

def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)

new_product_dict = {
    'Apple': 1,
    'Ice Cream': 3,
    'Chocolate': 5,
    }

# Call create_product() by passing new_product_dict
# as kwargs!
print(create_products(**new_product_dict))


