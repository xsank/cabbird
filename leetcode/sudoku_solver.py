def solveSudoku(board):
    for i,row in enumerate(board):
        board[i]=list(row[0])
    solve(board)
    prettyPrint(board)

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                for k in range(9):
                    board[i][j]=str(k+1)
                    if isValid(board,i,j):
                        prettyPrint(board)
                        solve(board)
                    else:
                        board[i][j]="."
                return

def isValid(board,x,y):
    for i in range(9):
        if i!=x and board[i][y]==board[x][y]:
            return False
    for j in range(9):
        if j!=y and board[x][j]==board[x][y]:
            return False
    xi=x/3
    yi=y/3
    for i in range(xi*3,(xi+1)*3):
        for j in range(yi*3,(yi+1)*3):
            if i!=x and j!=y and board[i][j]==board[x][y]:
                return False
    return True


def prettyPrint(board):
    print '%s\r' % '\n'.join([''.join(i) for i in board]),
            

if __name__=="__main__":
    #solveSudoku([[".87654321"],["2........"],["3........"],["4........"],["5........"],["6........"],["7........"],["8........"],["9........"]])
    solveSudoku([["..9748..."],["7........"],[".2.1.9..."],["..7...24."],[".64.1.59."],[".98...3.."],["...8.3.2."],["........6"],["...2759.."]])
