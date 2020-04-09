'''
username and password generators
'''
def username_generator(first_name,last_name):
    first_name = first_name[:3] if len(first_name) >= 3 else first_name
    last_name = last_name[:4] if len(last_name) >= 4 else last_name
    return first_name + last_name

def password_generator(username):
    return username[-1] + username[:-1]

'''
split string of names into list of names, then split again to take only the last names
'''
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(", ")
print(author_names)
author_last_names = [i.split()[-1] for i in author_names]
print(author_last_names)

'''
split by lines and tabs via split('\n') and split('\t') respectively.
'''

'''
join via ',' to make csv's, join via '\n' to print lines:
'''
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

'''
strip extra spaces, then join by lines
'''
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [i.strip() for i in love_maybe_lines]

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

'''
1. find index of specific string within string
2. replace string within string
'''
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

disown_to_dethrone = god_wills_it_line_one.replace('disown', 'dethrone')
print(disown_to_dethrone)

'''
format a string based on input parameters - in one line without concatenation
'''
def poem_title_card(poet,title):
    return "The poem \"{}\" is written by {}.".format(title,poet)

'''
use keywords to allow flexibility in parameter/argument mapping.
the .format method fills in the wildcards based on the parameter that fits the name rather than the order
'''
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

my_beard_description = poem_description("1974","Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)