def set_zero(matrix):
    rows={}
    col={}
    for i,_ in enumerate(matrix):
        for j,nj in enumerate(matrix[i]):
            if nj==0:
                rows[i]=1
                col[j]=1
    for i,_ in enumerate(matrix):
        for j,_ in enumerate(matrix[i]):
            if rows.get(i) or col.get(j):
                matrix[i][j]=0
    return matrix


print set_zero([[1,1,1,1],[1,0,1,1],[1,1,1,0],[1,1,1,1]])
