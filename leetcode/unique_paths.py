
def rec_uniquePaths(m, n):
    if m==1 or n==1:
        return 1
    return uniquePaths(m-1,n)+uniquePaths(m,n-1)

def uniquePaths(m, n):
    grid=[[1]*n for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j]=grid[i-1][j]+grid[i][j-1]
    return grid[m-1][n-1]

if __name__=="__main__":
    print rec_uniquePaths(3,7)
    print uniquePaths(3,7)
    print uniquePaths(100,100)
