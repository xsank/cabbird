
def spiralOrder(matrix):
    if not matrix:
        return []
    top=0
    right=len(matrix[0])
    bottom=len(matrix)
    left=0
    total=[]
    while bottom>top and right>left:
        for i in range(left,right):
            total.append(matrix[top][i])
        top+=1
        for i in range(top,bottom):
            total.append(matrix[i][right-1])
        right-=1
        if bottom!=top:
            for i in range(right-1,left-1,-1):
                total.append(matrix[bottom-1][i])
        bottom-=1
        if right!=left:
            for i in range(bottom-1,top-1,-1):
                total.append(matrix[i][left])
        left+=1
    return total


if __name__=="__main__":
    print spiralOrder([
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ])
    print spiralOrder([])
    print spiralOrder([[1]])
    print spiralOrder([[1,2]])
    print spiralOrder([
     [1,2],
     [3,4]
    ])
    print spiralOrder([
     [7],
     [9],
     [6]
    ])
    print spiralOrder([
     [7],
     [9],
    ])
    print spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
