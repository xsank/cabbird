
def rotate(matrix):
    size=len(matrix)
    if size<=1:
        return
    tmp=[i[:] for i in matrix]
    for row in range(size):
        for column in range(size):
            matrix[row][column]=tmp[size-column-1][row]

if __name__=="__main__":
    print rotate([[1,2,3],[4,5,6],[7,8,9]])
    print rotate([])
    print rotate([1])
