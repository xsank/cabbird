def largestNumber(nums):
    sort_nums=sorted([str(i) for i in nums],cmp=sortStrNumber)
    return '0' if sort_nums[0]=='0' else ''.join(sort_nums)
    
    
def sortStrNumber(a,b):
    a_b=int(a+b) 
    b_a=int(b+a)
    return b_a-a_b
    
    
if __name__=="__main__":
    print largestNumber([3, 30, 34, 5, 9])
    print largestNumber([9,89,98])
    print largestNumber([1,1,1])
    print largestNumber([0,0,1])
    print largestNumber([0,0,0])
    print largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])