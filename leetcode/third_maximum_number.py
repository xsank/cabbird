import heapq


def thirdMax(nums):
    set_nums=set(nums)
    if len(set_nums)<3:
        return max(set_nums)
    return heapq.nlargest(3,set_nums)[-1]


if __name__=="__main__":
    print thirdMax([1,2])
    print thirdMax([1,2,3])
    print thirdMax([1,2,3,4,5])
    print thirdMax([1,2,2,5,3,5])
