
def findKthLargest(nums, k):
    sorted_nums=sorted(nums,reverse=True)
    return sorted_nums[k-1]


if __name__=="__main__":
    print findKthLargest([3,2,1,5,6,4],2)
