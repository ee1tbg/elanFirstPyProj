'''
Created on Apr 10, 2019

@author: Winterberger
'''
class SortedList(list):
  
  #def __init__(self, lst):
  #  self.selfsort()
  
  def selfsort(self):
    srtd = [0 for i in range(len(self))]
    index = 0
    while len(self) > 0:
      mindex = self.index(min(self))
      #print(mindex)
      #print(self[mindex])
      #print(min(self))
      srtd[index] = (min(self))
      self.pop(mindex)
      index += 1
      #print("\n sorted:")
      #print(srtd)
      #print("self:")
      #print(self)
    self = srtd
    print("Final self")
    print(self)
    return self
    
  def append(self, value):
    super().append(value)
    self.selfsort()
    return self
    
myList = SortedList([2,1])
print(myList)
myList.append(3)
print(myList)