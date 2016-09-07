def findPeakElement(nums):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)/2
        ln,rn=nums[mid-1],nums[mid+1]
        if nums[mid]>ln and nums[mid]>rn:
            return mid
        elif nums[mid]>rn and nums[mid]<ln:
            right=mid-1
        elif nums[mid]>ln and nums[mid]<rn:
            left=mid+1
        else:
            if rn>=ln:
                left=mid+1
            else:
                right=mid-1
    return left


if __name__=="__main__":
    print findPeakElement([1, 2, 3, 1])
    print findPeakElement([1, 2])
    print findPeakElement([1, 2, 3])
    print findPeakElement([1, 2, 1])
    print findPeakElement([1, 2, 1, 2, 1])
