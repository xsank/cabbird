
def searchRange(nums, target):
    start=0
    end=len(nums)-1
    res=[]
    while start<=end:
        if nums[start]==nums[end]==target:
            res.append(start)
            res.append(end)
            break
        if nums[start]!=target:
            start+=1
        if nums[end]!=target:
            end-=1
    if not res:
        res=[-1,-1]
    return res


if __name__=="__main__":
    print searchRange([1],0)
