def intersect(nums1, nums2):
    res=[]
    for i in nums1:
        if i in nums2:
            nums2.remove(i)
            res.append(i)
    return res
    
    
if __name__=="__main__":
    print intersect([1, 2, 2, 1],[2, 2])
    print intersect([1,2,2,1],[2])