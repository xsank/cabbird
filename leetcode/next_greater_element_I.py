def nextGreaterElement(findNums, nums):
    res=[]
    if findNums:
        _map={}
        length=len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]<nums[j]:
                    _map[nums[i]]=nums[j]
                    break
                else:
                    _map[nums[i]]=-1
        _map[nums[i+1]]=-1
        for fn in findNums:
            res.append(_map[fn])
    return res


if __name__=="__main__":    
    print nextGreaterElement([],[])
    print nextGreaterElement([4,1,2],[1,3,4,2])
    print nextGreaterElement([2,4],[1,2,3,4])
    print nextGreaterElement([1,3,5,2,4,7],[6,5,4,3,2,1,7])
