'''
Created on Jan 23, 2019

@author: Winterberger
'''

'''
Find unique letters in a string
'''
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    unique = ""
    for i in range(len(word)):
        if unique.find(word[i]) == -1:
            unique += word[i]
            #print unique
            return len(unique)
# Uncomment these function calls to test your function:
print(unique_english_letters("miSsissIppi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

'''
Count occurances of letter (substring) in string
'''
# Write your count_char_x function here:
def count_char_x(word,x):
    return word.count(x)
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

'''
Return substring between start and end string, with error handling
'''
# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
    if word.find(start) == -1 or word.find(end) == -1 or word.find(end) < word.find(start):
        return word
    else:
        return word[word.find(start)+1:word.find(end)]
    
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

'''
Return if all words in string are >= specified length
'''
# Write your x_length_words function here:
def x_length_words(sentence,x):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) < x:
            return False
    return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True