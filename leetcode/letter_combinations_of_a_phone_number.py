
def letterCombinations(digits):
    map={
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
    res=[]
    for c in digits:

