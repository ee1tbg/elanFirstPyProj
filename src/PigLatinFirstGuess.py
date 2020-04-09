'''
Created on Sep 16, 2018

@author: Winterberger
'''
word = input("Enter a word: ")
if len(word) < 2: #or type(word) != str:
    print ("Please enter a valid word next time")
    print ("You entered a " + str(type(word)) + " of length " + str(len(word)) + ".")
else:
    print ("You entered " + word + ".")
    etterpay = word[0]
    for x in range(0, len(word)-1):
        print ("replacing " + str(word[x]) + " with " + str(word[x+1]) + ".")
        word[x] = word[x+1]
    print ("Translated to: " + str(word) + "ay")