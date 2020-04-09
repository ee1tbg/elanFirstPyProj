'''
Created on Sep 16, 2018

@author: Winterberger
'''
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
    first = word[0]
    second = word[1].upper()
    new_word = second + word[2:len(word)] + first + pyg
    print (new_word)
else:
    print ('empty')