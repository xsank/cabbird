def nextGreaterElements(nums):
    res=[]
    if nums:
        length=len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]<nums[j]:
                    break
                else:
                    _map[nums[i]]=-1
        _map[nums[i+1]]=-1
        for fn in findNums:
            res.append(_map[fn])
    return res


if __name__=="__main__":    
    print nextGreaterElement([1,2,1])
