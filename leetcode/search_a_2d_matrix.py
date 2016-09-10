def searchMatrix(matrix, target):
    row=len(matrix)
    colume=len(matrix[0])
    rleft=0
    rright=row-1
    cleft=0
    cright=colume-1
    while rleft<=rright:
        rmiddle=(rleft+rright)/2
        if matrix[rmiddle][0]<=target and matrix[rmiddle][colume-1]>=target:
            while cleft<=cright:
                cmiddle=(cleft+cright)/2
                if matrix[rmiddle][cmiddle]>target:
                    cright=cmiddle-1
                elif matrix[rmiddle][cmiddle]<target:
                    cleft=cmiddle+1
                else:
                    return True
            return False
        elif matrix[rmiddle][0]>target:
            rright=rmiddle-1
        elif matrix[rmiddle][colume-1]<target:
            rleft=rmiddle+1
    return False


if __name__=="__main__":
    print searchMatrix([
      [1,   3,  5,  7],
        [10, 11, 16, 20],
          [23, 30, 34, 50]
          ],112)
    print searchMatrix([[1]],2)
    print searchMatrix([[1,2]],1)
    print searchMatrix([[1],[2]],1)
