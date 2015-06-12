
def setZeroes(matrix):
    if not matrix:
        return []
    row=len(matrix)
    column=len(matrix[0])
    rows=set()
    columns=set()
    for i in range(row):
        for j in range(column):
            if matrix[i][j]==0:
                rows.add(i)
                columns.add(j)
    for c in columns:
        for i in range(row):
            matrix[i][c]=0
    for r in rows:
        for j in range(column):
            matrix[r][j]=0
    return matrix


if __name__=="__main__":
    print setZeroes([])
    print setZeroes([[1]])
    print setZeroes([[1,2],[0,3]])
    print setZeroes([[1,2,3],[4,0,6],[7,8,9]])
