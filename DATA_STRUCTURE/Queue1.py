from collections import deque
class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,element):
        self.buffer.appendleft(element)
        print(element)
    def deque1(self):
        return self.buffer.pop()
    def Display(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
#element = [12,31,33,44,55]
qu=Queue()
qu.enqueue({
    'name':"ishtehar",
    'surname':'khan',
    'mobile':908777712
    
})
qu.enqueue({
    'name':"bajaj",
    'surname':'khan',
    'mobile':908777742
    
})
qu.enqueue({
    'name':"kishan",
    'surname':'khan',
    'mobile':908777710
    
})



qu.size()
qu.deque1()

        