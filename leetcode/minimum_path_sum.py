
def minPathSum(grid):
    m=len(grid)
    n=len(grid[0])
    MAX_NUM=1<<31
    res=[[MAX_NUM]*(n+1) for i in range(m+1)]
    res[0][0]=res[0][1]=res[1][0]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            res[i][j]=grid[i-1][j-1]+min(res[i][j-1],res[i-1][j])
    return res[m][n]


if __name__=="__main__":
    print minPathSum([[1,2,3]])
    print minPathSum([[1,2],[3,4]])
    print minPathSum([[1,1],[2,7],[2,8]])

