class MyQueue(object):
    def __init__(self):
        self.q=[]

    def push(self,x):
        self.q.append(x)

    def peek(self):
        return self.q[0]

    def pop(self):
        return self.q.pop(0)

    def empty(self):
        return not self.size()

    def size(self):
        return len(self.q)


class MyStack(object):
    def __init__(self):
        self.q=MyQueue()

    def push(self,x):
        self.q.push(x)

    def pop(self):
        length=self.q.size()
        for i in range(length-1):
            self.q.push(self.q.pop())
        return self.q.pop()
    
    def top(self):
        length=self.q.size()
        t=-1
        for i in range(length):
            t=self.q.pop()
            self.q.push(t)
        return t

    def empty(self):
        return self.q.empty()


if __name__=="__main__":
    stack=MyStack()
    stack.push(1)
    stack.push(2)
    print stack.pop()
    print stack.top()
    print stack.empty()
