
def findMin(nums):
    start=0
    end=len(nums)-1
    _min=nums[start]
    while start<=end:
        mid=(start+end)/2
        if nums[end]>=nums[mid]>=nums[start]:
            _min=nums[start]
            break
        if nums[mid]>=nums[start]>nums[end]:
            start=mid+1
        if nums[mid]<=nums[end]<nums[start]:
            end=mid
    return _min

if __name__=="__main__":
    print findMin([4,5,6,7,0,1,2])
    print findMin([4,5,6,7])
    print findMin([4])
    print findMin([4,5])
    print findMin([2,3,1])
    print findMin([2,1])
    print findMin([3,1,2])
