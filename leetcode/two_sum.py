
def twoSum(num,target):
    dic={}
    res=[]
    for index,item in enumerate(num):
        dic[index+1]=item
    sorted_dict=sorted(dic.iteritems(),key=lambda v:v[1],reverse=False)
    head=0
    tail=len(sorted_dict)-1
    while head<tail:
        hn=sorted_dict[head][1]
        tn=sorted_dict[tail][1]
        if hn+tn<target:
            head+=1
        elif hn+tn==target:
            res=sorted([sorted_dict[head][0],sorted_dict[tail][0]])
            break
        else:
            tail-=1
    return res


if __name__=="__main__":
    print twoSum([0,4,3,0],0)
