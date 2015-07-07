
class Queue:
    def __init__(self):
        self.queue=[]
        
    def push(self,x):
        self.queue.append(x)
        
    def pop(self):
        if self.queue:
            return self.queue.pop(0)    
        return -1
        
    def peek(self):
        if self.queue:
            return self.queue[0]
        return -1
       
    def empty(self):
        return not self.queue
        
        
if __name__=="__main__":
    q=Queue()
    q.push(1)
    q.push(2)
    print q.peek()
    print q.pop()
    print q.empty()
    print q.peek()
    print q.pop()
    print q.empty()