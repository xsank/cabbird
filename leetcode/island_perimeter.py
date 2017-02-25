def islandPerimeter(grid):
    direction=[(-1,0),(1,0),(0,-1),(0,1)]
    res=0
    h=len(grid)
    w=len(grid[0])
    for i in range(h):
        for j in range(w):
            if grid[i][j]:
                tn=4
                for ti,tj in direction:
                    ni=i+ti
                    nj=j+tj
                    if h>ni>=0 and w>nj>=0 and grid[ni][nj]:
                        tn-=1
                res+=tn
    return res


if __name__=="__main__":
    print islandPerimeter(
        [[0,1,0,0],
         [1,1,1,0],
          [0,1,0,0],
           [1,1,0,0]]
    )
