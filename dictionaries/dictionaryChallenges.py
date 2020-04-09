'''
Created on Feb 1, 2019

@author: Winterberger
'''
# Write your values_that_are_keys function here:
import dictionaryBasics
def values_that_are_keys(my_dictionary):
    return [my_dictionary[key] for key in my_dictionary if my_dictionary[key] in my_dictionary.keys()]
'''
for key in my_dictionary:
  if my_dictionary[key] in my_dictionary.keys():
    valkeys.append(my_dictionary[key])
return valkeys
'''
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


'''
Determine frequency of each entry in a list. return a dictionary with key = entry and value = frequency
'''
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    freq_dict = {}
    for i in range(len(words)):
        if words[i] not in words[i+1:]:
            key_count = 0
            key = words[i]
            #print(key)
            for j in words:
                #print(j)
                if key == j:
                    key_count += 1
                    #print(key_count)
        freq_dict.update({key:key_count})
        #print(freq_dict)
    return freq_dict
'''        
  keys = [words[index] for index in range(len(words)) if words[index] not in words[index+1:]]
  print(keys)
  frequency = []
'''
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

'''
Count number of unique values in a dictionary
'''
# Write your unique_values function here:
def unique_values(my_dictionary):
    val_list = [lVal for lVal in my_dictionary.values()]
    print(val_list)
    unique_vals = [val_list[i] for i in range(len(val_list)) if val_list[i] not in val_list[i+1:]]
    print(unique_vals)
    num_unique_vals = len(unique_vals)
    return num_unique_vals
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

'''
Last name nightmare...
'''
# Write your count_first_letter function here:
def count_first_letter(names):
  last_names = [i for i in names]
  first_names = [names[i] for i in last_names]
  print(last_names)
  print(first_names)
  last_letters = [last_name[0] for last_name in last_names]
  print(last_letters)
  for i in range(len(last_names)):
    if last_letters[i] in last_letters[:i]:
      index = last_letters.index(last_letters[i])
      first_names[i] += first_names[index]
      last_letters.pop(index)
      first_names.pop(index)
      print(last_letters)
      print(first_names)
  new_names = {last_letter:names for last_letter,names in zip(last_letters,first_names)}
  return new_names
# Uncomment these function calls to test your  function:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}