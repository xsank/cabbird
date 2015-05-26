
def containsDuplicate(nums):
    if not nums:
        return False
    return len(nums)!=len(set(nums))


if __name__=="__main__":
    print containsDuplicate([1,1])
