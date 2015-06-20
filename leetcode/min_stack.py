class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self,x):
        self.stack.append(x)
        if not self.minStack or self.minStack[-1]>=x:
            self.minStack.append(x)
        return x

    def pop(self):
        if self.stack:
            if self.stack.pop()==self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        return -1


if __name__=="__main__":
    ms=MinStack()
    ms.push(2)
    ms.push(0)
    ms.push(3)
    ms.push(0)
    print ms.getMin()
    print ms.top()
    ms.pop()
    print ms.getMin()
    ms.pop()
    print ms.getMin()
    ms.pop()
    print ms.getMin()
    print ms.top()
