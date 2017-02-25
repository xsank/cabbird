def minMoves2(nums):
    _min=min(nums)
    _max=max(nums)
    res=1<<31
    for i in range(_min,_max+1):
        t=sum([abs(j-i) for j in nums])
        if t<res:
            res=t
    return res


def _minMoves2(nums):
    nums.sort()
    median=nums[len(nums)/2]
    return sum(abs(n-median) for n in nums)
            

if __name__=="__main__":
    print minMoves2([1,2,3])
    print minMoves2([-1,2,3])
    print minMoves2([2,2,3])
    print minMoves2([3,3,3])
