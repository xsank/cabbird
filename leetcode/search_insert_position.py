
def searchInsert(nums, target):
    start=0
    end=len(nums)-1
    if nums[start]>=target:
        return start
    if nums[end]<target:
        return end+1
    while start<=end:
        if nums[start]==nums[end]==target:
            break
        if nums[start]<target:
            start+=1
        if nums[end]>target:
            end-=1
    return start


if __name__=="__main__":
    print searchInsert([1,3,5,6],5)
    print searchInsert([1,3,5,6],2)
    print searchInsert([1,3,5,6],7)
    print searchInsert([1,3,5,6],0)
    print searchInsert([1,3],3)

