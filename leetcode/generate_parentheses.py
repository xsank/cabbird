def generateParenthesis(n):
    total=[]
    genParenthesis(total,["("],n-1,n)
    return total
            
            
def genParenthesis(total,res,left,right):
    if left>0:
        if left<right:
            lres=res[:]
            lres.append("(")
            genParenthesis(total,lres,left-1,right)
            rres=res[:]
            rres.append(")")
            genParenthesis(total,rres,left,right-1)
        else:
            res.append("(")
            genParenthesis(total,res,left-1,right)
    else:
        for i in range(right):
            res.append(")")
        total.append(''.join(res))
    
   
    
    
    
if __name__=="__main__":
    print generateParenthesis(3)
    print generateParenthesis(1)
    print generateParenthesis(2)
    print generateParenthesis(4)