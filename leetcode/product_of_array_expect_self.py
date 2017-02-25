def productExceptSelf(nums):
    length=len(nums)
    res=[1 for i in range(length)]
    t=1
    for i in range(length-1,0,-1):
        t*=nums[i]
        res[i-1]*=t
    t=1
    for i in range(0,length-1):
        t*=nums[i]
        res[i+1]*=t
    return res


if __name__=="__main__":
    print productExceptSelf([1,2,3,4])
