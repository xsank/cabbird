
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
        total[0]+=1
        return
    for col in range(size):
        if isAblePlace(board,row,col,size):
            board[row][col]='Q'
            findAllPositions(total,board,row+1,size)
            board[row][col]='.'

def totalNQueens(n):
    board=[['.']*n for i in range(n)]
    total=[0]
    findAllPositions(total,board,0,n)
    return total[0]




if __name__=="__main__":
    print totalNQueens(1)
    print totalNQueens(2)
    print totalNQueens(3)
    print totalNQueens(4)
    print totalNQueens(8)
