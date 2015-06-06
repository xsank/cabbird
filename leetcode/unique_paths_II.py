
def uniquePathsWithObstacles(obstacleGrid):
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    if m==1:
        return 0 if 1 in obstacleGrid[0] else 1
    if n==1:
        return 0 if [1] in obstacleGrid else 1
    if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]:
        return 0
    grid=[[1]*n for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i-1][j]==1:
                if i==1:
                    for k in range(j,n):
                        grid[0][k]=0
                else:
                    grid[i-1][j]=0
            if obstacleGrid[i][j-1]==1:
                if j==1:
                    for k in range(i,m):
                        grid[k][0]=0
                else:
                    grid[i][j-1]=0
            grid[i][j]=grid[i-1][j]+grid[i][j-1]
    return grid[m-1][n-1]

if __name__=="__main__":
    print uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print uniquePathsWithObstacles([[0,0,0]])
    print uniquePathsWithObstacles([[0,1,0]])
    print uniquePathsWithObstacles([[0],[0],[0]])
    print uniquePathsWithObstacles([[0,0],[0,1]])
    print uniquePathsWithObstacles([[0,1],[1,0]])
    print uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
