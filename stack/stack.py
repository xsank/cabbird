class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return bool(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        else:
            return self.pop()

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

    def is_empty(self):
        return bool(self.top)

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

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
