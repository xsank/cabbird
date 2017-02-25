def reconstructQueue(people):
    res=[]
    index=0
    for i in people:
        if i[1]>=len(res):
            res.append(i)
        else:
            t=0
            flag=False
            for n,j in enumerate(res):
                if i[1]==t:
                    res.insert(n,i)
                    flag=True
                    break
                if j[0]>=i[0] :
                    t+=1
            if not flag:
                res.append(i)
    return res
            

if __name__=="__main__":
    print reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    print reconstructQueue([[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]])
