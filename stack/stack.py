class Stack:
    def __init__(self):
        self.items=[]

    def __iter__(self):
        for item in self.items:
            yield item

    def is_empty(self):
        return not self.items

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.__init__()


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedStack:
    def __init__(self):
        self.top=None
        self._size=0

    def __iter__(self):
        tmp=self.top
        while tmp:
            yield tmp.value
            tmp=tmp.next


    def is_empty(self):
        return not self.top

    def pop(self):
        node=self.top
        if node:
            self.top=node.next
            self._size-=1
            return node.value
        else:
            raise Exception('Stack is empty!')

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node
        self._size+=1

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.top.value

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
