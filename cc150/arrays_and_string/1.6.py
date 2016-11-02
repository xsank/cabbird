def rotate_matrix(matrix):
    length=len(matrix)
    for i in range(length/2):
        first=i
        last=length-1-i
        for j in range(first,last):
            offset=j-first
            top=matrix[first][j]
            matrix[first][j]=matrix[last-offset][first]
            matrix[last-offset][first]=matrix[last][last-offset]
            matrix[last][last-offset]=matrix[j][last]
            matrix[j][last]=top
    return matrix


print rotate_matrix([[1,2],[3,4]])
print rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
