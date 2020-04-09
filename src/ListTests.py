'''
Created on Jan 1, 2019

@author: Winterberger
'''

'''
Double specified index of a list
'''
#Write your function here
def double_index(lst, index):
    try:
        lst[index] *= 2
    except IndexError:
        print("Invalid index")
    return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

'''
Remove specified chunk from list
'''
#Write your function here
def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

'''
Does a list contain 'item' more than specified number of times?
'''
#Write your function here
def more_than_n(lst,item,n):
    return lst.count(item) > n

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

'''
Return the item that appears more frequently in list
'''
#Write your function here
def more_frequent_item(lst,item1,item2):
    return item1 if lst.count(item1) >= lst.count(item2) else item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

'''
Return middle element (or average of middle 2)
'''
#Write your function here
def middle_element(lst):
    if 0 == len(lst) % 2:
        item1 = lst[int(len(lst)/2-1)]
        item2 = lst[int(len(lst)/2)]
        return (item1 + item2) / 2
    else:
        ind = int((len(lst)+1)/2 - 1)
        return lst[ind]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5,2,-4,4,5]))

'''
Fibonacci
'''
#Write your function here
def append_sum(lst):
    for i in range(3):
        lst.append(int(lst[-1])+int(lst[-2]))
    return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

'''
Return last element of larger of 2 lists
'''
#Write your function here
def larger_list(lst1,lst2):
    return lst1[-1] if len(lst1) >= len(lst2) else lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

'''
Combine and sort 2 lists
'''
#Write your function here
def combine_sort(lst1,lst2):
    return sorted(lst1+lst2)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

'''
Append length of list to list, return list
'''
#Write your function here
def append_size(lst):
    lst.append(len(lst))
    return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

'''
Return every xth number from start to end
'''
#Write your function here
def every_x_nums(start,end,num):
    return list(range(start,end+1,num))

#Uncomment the line below when your function is done
print(every_x_nums(91,100,3))
