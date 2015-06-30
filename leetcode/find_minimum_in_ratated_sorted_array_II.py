
def findMin(nums):
    start=0
    end=len(nums)-1
    _min=nums[start]
    while start<=end:
        mid=(start+end)/2
        if nums[end]>=nums[mid]>=nums[start]:
            if nums[end]!=nums[start] or start==end:
                _min=nums[start]
                break
            else:
                start+=1
                continue
        if nums[mid]>=nums[start]>=nums[end]:
            start=mid+1
        if nums[mid]<=nums[end]<=nums[start]:
            end=mid
    return _min

if __name__=="__main__":
    print findMin([4,5,6,7,0,1,2])
    print findMin([1,2,3,3,3,3,3])
    print findMin([3,3,1,2,3,3,3])
    print findMin([3,3,3,3,3,1,2])
    print findMin([3,1,3])
    print findMin([3,3,1,3])
    print findMin([3,3,4,3])
    print findMin([2,2,0,0,1,1,1])
