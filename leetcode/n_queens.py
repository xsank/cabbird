
def isAblePlace(board,row,col,size):
    for i in range(row):
        if board[i][col]=='Q':
            return False
        if col-i-1>=0 and board[row-i-1][col-i-1]=='Q':
            return False
        if col+i+1<size and board[row-i-1][col+i+1]=='Q':
            return False
    return True

def findAllPositions(total,board,row,size):
    if row==size:
        total.append([''.join(i) for i in board])
        return
    for col in range(size):
        if isAblePlace(board,row,col,size):
            board[row][col]='Q'
            findAllPositions(total,board,row+1,size)
            board[row][col]='.'

def solveNQueens(n):
    board=[['.']*n for i in range(n)]
    total=[]
    findAllPositions(total,board,0,n)
    return total




if __name__=="__main__":
    print solveNQueens(1)
    print solveNQueens(2)
    print solveNQueens(3)
    print solveNQueens(4)
    #print solveNQueens(8)
