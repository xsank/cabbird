
def trap(height):
    start=0
    end=len(height)-1
    left=0
    right=0
    if end<=0:
        return 0
    _max_index=height.index(max(height))
    _sum=0
    while start<=_max_index:
        if height[start]>=left:
            left=height[start]
        else:
            _sum+=(left-height[start])
        start+=1
    while end>=_max_index:
        if height[end]>=right:
            right=height[end]
        else:
            _sum+=(right-height[end])
        end-=1
    return _sum


if __name__=="__main__":
    print trap([0,1,0,2,1,0,1,3,2,1,2,1])
