def lexicalOrder(n):
    res=[]
    stack=[1]
    while stack:
        x=stack.pop()
        res.append(x)
        t2=x+1
        if t2<=n and t2%10:
            stack.append(t2)
        t1=x*10
        if t1<=n:
            stack.append(t1)
    return res


if __name__=="__main__":
    print lexicalOrder(13)
    print lexicalOrder(5000)
