class LFUCache(object):
    
    def __init__(self,capacity):
        self.capacity=capacity
        self.dic={}
        self.queue=[]

    def _update(self,key):
        self.queue.remove(key)
        self.queue.append(key)

    def get(self,key):
        if key in self.dic:
            self._update(key)
            return self.dic[key]
        return -1

    def set(self,key,value):
        if self.capacity>0:
            if len(self.queue)==self.capacity:
                del self.dic[self.queue[0]]
                self.queue.pop(0)
            :self.queue.append(key)
            self.dic[key]=value


if __name__=="__main__":
    cache=LFUCache(2)
    cache.set(1, 1);
    cache.set(2, 2);
    print cache.get(1);       # returns 1
    cache.set(3, 3);    # evicts key 2
    print cache.get(2);       # returns -1 (not found)
    print cache.get(3);       # returns 3.
    cache.set(4, 4);    # evicts key 1.
    print cache.get(1);       # returns -1 (not found)
    print cache.get(3);       # returns 3
    print cache.get(4);       # returns 4
    cache=LFUCache(0)
    print cache.get(1)
    cache.set(1, 1)
