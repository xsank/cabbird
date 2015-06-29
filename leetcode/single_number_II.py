
def singleNumber(nums):
    total_set=set(nums)
    _dict={}
    for i in total_set:
        _dict[i]=0
    res=-1
    for i in nums:
        _dict[i]+=1
    for k,v in _dict.items():
        if v==1:
            res=k
            break
    return res


if __name__=="__main__":
    print singleNumber([43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43])
