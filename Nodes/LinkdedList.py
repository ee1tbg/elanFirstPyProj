'''
Created on Jul 22, 2019

@author: Winterberger
'''
# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove, instance=0):
    index = 0
    current_node = self.head_node
   
    # special case if first node is to be removed
    if (self.head_node.value == value_to_remove) and (instance == 0):
      self.head_node = current_node.get_next_node()
    else:
      'otherwise loop until value is found at desired index - as long as current_node is defined'
      while (current_node.get_next_node()) and ((current_node.get_next_node().get_value() != value_to_remove) or (index < instance)):
        ' iterate index if match is found'
        if current_node.get_next_node().get_value() == value_to_remove:
          index+=1
          
        ' set new node'
        current_node = current_node.get_next_node()
        
          
      ' If match is found at desired instance'
      if current_node.get_next_node().get_value() is value_to_remove:
        current_node.set_next_node(current_node.get_next_node().get_next_node())