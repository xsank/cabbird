class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('Queue is empty!')
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def clear(self):
        self.__init__()


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedQueue:
    def __init__(self):
        self.front=None
        self.back=None
        self._size=0

    def is_empty(self):
        return self._size==0

    def enqueue(self,value):
        node=Node(value)
        if self.front:
            self.back.next=node
        else:
            self.front=node
        self.back=node
        self._size+=1

    def dequeue(self,value):
        if self.front:
            value=self.front.value
            self.front=self.front.next
            self._size-=1
            return value
        raise Exception('Queue is empty!')

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
