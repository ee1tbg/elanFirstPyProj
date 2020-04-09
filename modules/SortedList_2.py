'''
Created on Apr 10, 2019

@author: Winterberger
'''
class SortedList(list):
  
  def __init__(self, lst):
    self.selflist = lst
    print(self.selflist)
    self.selfsort()
    print(self)
  
  def selfsort(self):
    srtd = [0 for i in range(len(self.selflist))]
    index = 0
    while len(self.selflist) > 0:
      mindex = self.selflist(index(min(self.selflist)))
      #print(mindex)
      #print(self[mindex])
      #print(min(self))
      srtd[index] = (min(self.selflist))
      self.selflist.pop(mindex)
      index += 1
      #print("\n sorted:")
      #print(srtd)
      #print("self:")
      #print(self)
    self.selflist = srtd
    print("Final self")
    print(self)
    print(self.selflist)
    return self
    
  def append(self, value):
    super().append(value)
    self.selfsort()
    return self
    
myList = SortedList([2,1])
print(myList)
myList.append(3)
print(myList)