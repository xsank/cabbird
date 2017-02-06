_map={
        "1":"",
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
        "*":"",
        "0":" ",
        "#":"",
}
def letterCombinations(digits):
    res=[]
    findAll(digits,0,"",res)
    return res

def findAll(digits,cur,r,res):
    if cur==len(digits):
        res.append(r)
        return
    for c in _map[digits[cur]]:
        findAll(digits,cur+1,r+c,res)

if __name__=="__main__":
    print letterCombinations("23")
