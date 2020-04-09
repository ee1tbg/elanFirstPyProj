'''
Created on Nov 16, 2018

@author: Winterberger
'''
def repeat_stuff(stuff,num_repeats=10):
    return (stuff*num_repeats), stuff #stuff is returned just to show you can return multiple things like this

#need to define a 2nd variable 'discard' to set to the 2nd returned value from repeat_stuff().
#it is never used, hence its name
short_lyrics, discard = repeat_stuff("Row ",3)

lyrics = short_lyrics + "Your Boat. \n"

'''
again 'discard' is a dummy variable used to extract only the lyrics from 'repeat_stuff'
seems like this type of function (return multiple things when only one is needed) can be used
to protect it from being improperly used, or to use a CRC type thing (only use function output if one of its return variables is 'healthy'
'''
song,discard = repeat_stuff(lyrics)

print(song)