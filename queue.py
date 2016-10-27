from collections import deque
d = deque()
class Queue:
       def __init__(self):
           self.items = []
       def isEmpty(self):
           return self.items == []
   
       def enqueue(self, item):
           self.items.insert(0,item)
           d.append(item)
  
       def dequeue(self):
              if self.isEmpty() == True:
                 stat = 0
                 return str(stat)
              else :
                  return self.items.pop()   
                 #return self.items.remove(host)
       def deque(self,host):
              if self.isEmpty() == True:
                 stat = 0
                 return str(stat)
              else :
                 # return self.items.pop()
                 return self.items.remove(host)

       def size(self):
          return len(self.items)
       def inqueue(self,x):
          if not x in self.items:
            status = 1
          else :
            status = 2
          return status
       def lqueue(self):
              return self.items
