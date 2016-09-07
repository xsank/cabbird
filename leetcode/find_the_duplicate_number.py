def findDuplicate(nums):
    slow=0
    fast=0
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    fast=0
    while True:
        slow=nums[slow]
        fast=nums[fast]
        if slow==fast:
            break
    return fast


if __name__=="__main__":
    print findDuplicate([1,2,2])
