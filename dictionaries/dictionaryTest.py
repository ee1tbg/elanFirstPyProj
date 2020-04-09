'''
Created on Jan 31, 2019

@author: Winterberger
'''
myDict = {'key1':1,'key2':2,'key3':3,'key5':5}

print("Test 1:")
#Prints just the keys
for i in myDict:
    print(i)
    
'''
#Doesn't work
print("Test 2:")
for i,j in myDict:
    print(i,j)
''' 

#Prints keys and associated values
print("Test 3:")
for i in myDict:
    print(i,myDict[i])
    
#.pop doesn't return anything unless you PRINT it
myDict.pop('key4',"AHP")
print(myDict.pop('key4',"AHP"))

