def isValidSudoku(board):
    def isValid(line):
        return len(set(line))==len(line)

    def rmDot(n):
        return n!='.'

    length=len(board)
    for row in board:
        nrow=filter(rmDot,[n for n in row])
        if not isValid(nrow): 
            return False
    for i in range(length):
        row=filter(rmDot,[board[j][i] for j in range(length)])
        if not isValid(row):
            return False
    for i in range(length):
        if i%3==2:
            for j in range(length):
                if j%3==2:
                    sq=filter(rmDot,[board[ii][jj] for ii in range(i-2,i+1) for jj in range(j-2,j+1)])
                    if not isValid(sq):
                        return False
    return True
            

        


if __name__=="__main__":
    print isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
    print isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])
