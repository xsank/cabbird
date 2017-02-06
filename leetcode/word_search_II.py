def findWords(board, words):
    h=len(board)
    w=len(board[0])
    res=[]
    swords=set(words)
    for word in swords:
        for i in range(h):
            for j in range(w):
                if search(board,h-1,w-1,i,j,word,[]):
                    res.append(word)
    return res


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
    print findWords(["a"],["a","a"])    
    print findWords([
      ['o','a','a','n'],
        ['e','t','a','e'],
          ['i','h','k','r'],
            ['i','f','l','v']
            ],["oath","pea","eat","rain"])
