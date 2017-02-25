def maximalRectangle(matrix):
    h=len(matrix)
    w=len(matrix[0])
    visited=[[0]*w for i in range(h)]
    areas=[]
    dfs(matrix,h,w,0,0,areas,visited)
    return max(areas)


def dfs(matrix,h,w,i,j,areas,visited):
    th=i
    tw=j
    tarea=[]
    if matrix[i][j]=="1":
        for m in range(i,h):
            for n in range(j,w):
                if matrix[m][n]=="0":
                    tw=n-1

                


if __name__=="__main__":
    print maximalRectangle([
    ['1', '0', '1', '0', '0']
    ['1', '0', '1', '1', '1']
    ['1', '1', '1', '1', '1']
    ['1', '0', '0', '1', '0']
    ])
