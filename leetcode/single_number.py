
def singleNumber(nums):
    res=0
    for i in nums:
        res^=i
    return res


if __name__=="__main__":
    print singleNumber([1,1,2,2,3])
