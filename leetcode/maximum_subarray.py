
def maxSubArray(nums):
    _sum=0
    _max=-1<<31
    for i in nums:
        _sum+=i
        if i>=_sum:
            _sum=i
        if _sum>=_max:
            _max=_sum
    return _max

if __name__=="__main__":
    print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
