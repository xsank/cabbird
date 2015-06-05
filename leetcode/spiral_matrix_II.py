
def generateMatrix(n):
    if n<=0:
        return []
    total=[[0]*n for i in range(n)]
    top=0
    right=len(total[0])
    bottom=len(total)
    left=0
    index=0
    num=n*n
    while index<num:
        for i in range(left,right):
            index+=1
            total[top][i]=index
        top+=1
        for i in range(top,bottom):
            index+=1
            total[i][right-1]=index
        right-=1
        if bottom!=top:
            for i in range(right-1,left-1,-1):
                index+=1
                total[bottom-1][i]=index
        bottom-=1
        if right!=left:
            for i in range(bottom-1,top-1,-1):
                index+=1
                total[i][left]=index
        left+=1
    return total


if __name__=="__main__":
    print generateMatrix(3)
    print generateMatrix(1)
    print generateMatrix(2)
    print generateMatrix(4)
