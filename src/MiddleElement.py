'''
Created on Jan 1, 2019

@author: Winterberger
'''
#Write your function here
def middle_element(lst):
  #print(len(lst))
  #print(len(lst) % 2)
  if 0 == len(lst) % 2:
    ind1 = int(len(lst)/2-1)
    ind2 = int(len(lst)/2)
    item1 = lst[int(len(lst)/2-1)]
    item2 = lst[int(len(lst)/2)]
    print(ind1)
    print(ind2)
    print(item1)
    print(item2)
    return (item1 + item2) / 2
  else:
    #return lst[(len(lst)+1)/2 + 1]
    return True
  return False

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))