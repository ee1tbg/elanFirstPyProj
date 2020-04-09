'''
Created on Sep 8, 2018

@author: Winterberger
'''
def first_conditional_function(second_conditional):
    first_conditional = False
    second_conditional = True if (second_conditional == "True") else False
    if second_conditional == False:
        print ("You said " + str(second_conditional) + " but I want True.")
        first_conditional = True
        return first_conditional
    else:
        print ("You said " + str(second_conditional) + " and I like that one, so we'll keep it.")
        return second_conditional

#test_input = bool(input("Pick any Boolean"))
###integer_to_string_input = (input("Enter an integer: "))
test_input = (input("Pick any Boolean"))
print ("Default input details")
print (first_conditional_function(test_input))
   
    