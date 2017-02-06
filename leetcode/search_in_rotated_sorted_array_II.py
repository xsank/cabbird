def search(nums, target):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)/2
        if nums[mid]==target:
            return True
        if nums[mid]==nums[start]:
            start+=1
        elif nums[start]<nums[mid]:
            if target<nums[mid] and target>=nums[start]:
                end=mid-1
            else:
                start=mid+1
        else:
            if target>nums[mid] and target<=nums[end]:
                start=mid+1
            else:
                end=mid-1
    return False


if __name__=="__main__":
    print search([4,5,6,7,0,1,2,3],4)
    print search([1,3,1,1,1],4)
    print search([1,3,1,1,1],3)
    print search([1,3],3)
    print search([3,5,1],1)
    print search([3,1,2,2,2],1)

