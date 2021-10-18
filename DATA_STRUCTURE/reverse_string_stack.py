"""Write a function in python that can reverse a string using stack data structure"""
from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def isEmpty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def top(self):
        print(self.container[-1])

def reverse(s):
    stack=Stack()
    for ch in s:
        stack.push(ch)
    rev=''
    while stack.size()!=0:
        rev +=stack.pop()
    return rev
if __name__ == '__main__':
    print(reverse("hello my name is khan"))
    print(reverse("hello how are you"))


        