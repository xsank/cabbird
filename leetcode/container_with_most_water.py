
def maxArea(height):
    max_area=0
    start=0
    end=len(height)-1
    while start<end:
        tmp=(end-start)*min(height[start],height[end])
        if tmp>max_area:
            max_area=tmp
        if height[start]>height[end]:
            end-=1
        else:
            start+=1
    return max_area


if __name__=="__main__":
    print maxArea([1,2,3,4,5])
