
def trap(height):
    dic={}
    area=height[:]
    start=0
    end=len(height)-1
    left=0
    right=0
    if end<=0:
        return 0
    _max_index=height.index(max(height))
    while start<=_max_index:
        if height[start]>=left:
            left=height[start]
        else:
            dic[start]=left
        start+=1
    while end>=_max_index:
        if height[end]>=right:
            right=height[end]
        else:
            dic[end]=right
        end-=1
    for i,j in dic.items():
        area[i]=j
    return sum(area)-sum(height)


if __name__=="__main__":
    print trap([0,1,0,2,1,0,1,3,2,1,2,1])
