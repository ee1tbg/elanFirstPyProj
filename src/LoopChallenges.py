'''
Created on Jan 5, 2019

@author: Winterberger
'''

'''
list elements divisible by 10
'''
#Write your function here
def divisible_by_ten(nums):
    new = [i for i in nums if (i%10==0)]
    print(new)
    return len([i for i in nums if i%10==0])
#result = 0
#for i in nums:
#  if i%10==0:
#    result += 1
#return result

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

'''
Add greetings to list of names
'''
#Write your function here
def add_greetings(names):
    return ["Hello, " + i for i in names]

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

'''
Pop off first element of list until first element is odd
'''
#Write your function here
def delete_starting_evens(lst):
    while(len(lst)>0 and lst[0]%2==0):
        lst.pop(0)
    return lst
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

'''
create new list containing elements at odd indeces of old list
'''
#Write your function here
def odd_indices(lst):
    return [lst[i] for i in range(len(lst)) if i%2]
# the above line does the following:
def odd_indices_long(lst):
    new_list = []
    for i in range(len(lst)):
        if i%2:
            new_list.append(lst[i])
    return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

'''
raise bases from list 1 to powers from list 2. nested list comprehension!
'''
#Write your function here
def exponents(bases,powers):
    return [bases[i]**powers[j] for i in range(len(bases)) for j in range(len(powers))]

def exponents_long(bases, powers):
    lst = []
    for i in range(len(bases)):
        for j in range(len(powers)):
            lst.append(bases[i]**powers[j])
    return (lst)

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

'''
Return lst with larger sum
'''
#Write your function here
def larger_sum(lst1,lst2):
    return lst1 if sum(lst1) >= sum(lst2) else lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

'''
add items in list until sum exceeds a desired value
'''
#Write your function here
def over_nine_thousand(lst, val):
    if len(lst)==0:
        return 0
    else:
        sum_of_list = 0
        i = 0
        while sum_of_list <= val and i < len(lst):
            sum_of_list += lst[i]
            i+=1
    return sum_of_list

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000], 9000))

'''
return maximum number in list
'''
#Write your function here
def max_num(nums):
    max_num = nums[0]
    for i in nums:
        max_num = i if i > max_num else max_num
    return max_num

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

'''
return indeces of a set of lsts where the elements of those lsts at those indeces match
'''
#Write your function here
def same_values(lst1,lst2):
    return [i for i in range(len(lst1)) if lst1[i]==lst2[i]]

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

'''
Return TRUE if list1 is the reverse of list2
'''
#Write your function here
def reversed_list(lst1,lst2):
    is_reversed = True
    if len(lst1) != len(lst2):
        return False
    else:
        for i in range(len(lst1)):
            is_reversed &= lst1[i] == lst2[-i - 1]
    return is_reversed

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
