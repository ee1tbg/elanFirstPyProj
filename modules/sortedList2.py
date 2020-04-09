'''
Created on Apr 11, 2019

@author: Winterberger
'''
class SortedList(list):
  
  def __init__(self, lst):
    self = self.selfsort(lst)
    print("self from init:")
    print(self)
  
  def selfsort(self, lst):
    srtd = [0 for i in range(len(lst))]
    print(srtd)
    index = 0
    while len(lst) > 0:
      minval, mindex = min((minval, mindex) for (mindex, minval) in enumerate(lst))
      srtd[index] = minval
      lst.pop(mindex)
      index += 1
    self = srtd
    print("Final self")
    print(self)
    print(lst)
    return self
    
  def append(self, value):
    print("SELF")
    print(self)
    print(value)
    super().append(value)
    print("inlist")
    print(self)
    self = self.selfsort(self)
    #return self
    
myList = SortedList([2,1])
print("myList")
print(myList)
myList.append(3)
#print(myList)
