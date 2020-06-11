"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('.')
from singly_linked_list.singly_linked_list import LinkedList
class Stack:
    def __init__(self, data=[]):
        self.size = 0
        #self.storage = data
        self.storage = LinkedList()

    def __len__(self):
        #return len(self.storage)
        return self.size

    def push(self, value):
        # data = self.storage.append(value)
        # self.size = len(self.storage)
        # return data
        data = self.storage.add_to_tail(value)
        #self.size = self.storage.get_len()
        self.size += 1
        return data

    def pop(self):
        # if(len(self.storage)>0):
        #     data = self.storage.pop()
        #     self.size = len(self.storage)
        #     return data
        # else:
        #     pass
        if self.storage.get_len() > 0:
            data = self.storage.remove_tail()
            #self.size = self.storage.get_len()
            self.size -= 1
            return data
        else:
            pass

