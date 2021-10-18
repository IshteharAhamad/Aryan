from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return len (self.container==0)
    def size(self):
        return len(self.container)
    def top(self):
        print(self.container[-1])
st=Stack()
st.push(12)
st.top()
