
def search(nums, target):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)/2
        if nums[mid]==target:
            return mid
        if nums[start]<nums[mid] and nums[mid]<nums[end]:
            if nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        elif nums[start]>nums[mid]:
            if nums[mid]>target or nums[end]<target:
                end=mid-1
            else:
                start=mid+1
        else:
            if nums[mid]<target or nums[start]>target:
                start=mid+1
            else:
                end=mid-1
    return -1


if __name__=="__main__":
    print search([4,5,6,7,0,1,2,3],4)
    print search([1,3],0)
    print search([1,3],4)
    print search([1,3],1)
    print search([1,3],3)
    print search([1],1)
    print search([1],0)
    print search([1],2)
    print search([4,5,6,7,8,1,2,3],8)
    print search([6,7,8,1,2,3,4,5],7)

