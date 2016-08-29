import random


class Solution(object):
    def __init__(self,nums):
        self.nums=nums
        self.bak=nums[:]

    def reset(self):
        return self.bak

    def shuffle(self):
        length=len(self.nums)
        for i in range(length-1):
            t=random.randint(0,length-1)
            if t!=i:
                self.nums[i],self.nums[t]=self.nums[t],self.nums[i]
        return self.nums


if __name__=="__main__":
    solution=Solution([1,2,3])
    print solution.reset()
    print solution.shuffle()
