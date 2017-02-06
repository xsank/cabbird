def largestRectangleArea(heights):
    heights.append(0)
    stack=[0]
    res=0
    length=len(heights)
    for i in range(1,length):
        while stack and heights[i]<heights[stack[-1]]:
            h=heights[stack.pop()]
            w=i if not stack else i-stack[-1]-1
            res=max(res,w*h)
        stack.append(i)
    return res


if __name__=="__main__":
    print largestRectangleArea([2,1,5,6,2,3,1,1,1,1,1])
    print largestRectangleArea([2,1,5,6,2,3])
    print largestRectangleArea([1,2,3,4,5,6])
    print largestRectangleArea([6,5,4,3,2,1])
