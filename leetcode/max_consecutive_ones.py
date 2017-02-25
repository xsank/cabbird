def findMaxConsecutiveOnes(nums):
    _max=t=0
    for i in nums:
        if i==1:
            t+=1
        else:
            _max=max(_max,t)
            t=0
    return t if t>_max else _max 


if __name__=="__main__":
    print findMaxConsecutiveOnes([1,1,0,1,1,1])
