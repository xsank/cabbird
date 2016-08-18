def intersection(nums1, nums2):
    return list(set(nums1)&set(nums2))
    
    
if __name__=="__main__":
    print intersection([1, 2, 2, 1],[2, 2])