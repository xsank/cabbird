def exist(board, word):
    h=len(board)
    w=len(board[0])
    for i in range(h):
        for j in range(w):
            if search(board,h-1,w-1,i,j,word,[]):
                return True
    return False


def search(board,hi,wi,i,j,word,record):
    if board[i][j]==word[len(record)] and (i,j) not in record:
        record.append((i,j))
        if len(record)>=len(word):
           return True
        if i-1>=0 and search(board,hi,wi,i-1,j,word,record[:]):
                return True
        if i+1<=hi and search(board,hi,wi,i+1,j,word,record[:]):
                return True
        if j-1>=0 and search(board,hi,wi,i,j-1,word,record[:]):
                return True
        if j+1<=wi and search(board,hi,wi,i,j+1,word,record[:]):
                return True
    return False


if __name__=="__main__":
    print exist(["a"],"a")
    print exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"ABCCED")
    print exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"SEE")
    print exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"ABCB")
