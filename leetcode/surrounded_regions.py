def solve(board):
    if not board:
        return
    h=len(board)
    w=len(board[0])
    visited=[[0]*w for i in range(h)]
    direction=[(-1,0),(1,0),(0,-1),(0,1)]
    for m in range(1,h-1):
        for n in range(1,w-1):
            if board[m][n]=='O' and not visited[m][n]:
                queue=[(m,n)]
                surrounded=True
                points=[]
                while queue:
                    i,j=queue.pop()
                    if visited[i][j]:
                        continue
                    else:
                        visited[i][j]=1
                    points.append((i,j))
                    if i==0 or i==h-1 or j==0 or j==w-1:
                        surrounded=False
                    for di,dj in direction:
                        newi,newj=i+di,j+dj
                        if h-1>=newi>=0 and w-1>=newj>=0 and board[newi][newj]=="O":
                            queue.append((newi,newj))
                if surrounded:
                    for i,j in points:
                        board[i][j]="X"
    print board


if __name__=="__main__":
    solve([['X','O']])
    solve([['X','X'],['X','O']])
    solve([['O','O','O'],['O','O','O'],['O','O','O']])
    solve([['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']])
    solve([['X','X','X'],['X','O','X'],['X','X','X']])
