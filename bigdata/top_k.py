import string
import random
import hashlib
import collections


K=10

def rand_string():
    length=random.choice(range(1,len(string.digits)))
    return ''.join(random.sample(string.digits,length))+'\n'

def create_data(f=None,size=10000000):
    with open(f,'w') as f:
        while size:
            f.write(rand_string())
            size-=1

def devide_data(f=None,num=K):
    with open(f,'r') as f:
        tmp_files=[]
        for i in range(num):
            tmp_files.append(open(str(i),'w'))
        for s in f:
            tmp_files[int(hashlib.md5(s).hexdigest(),16)%num].write(s)
        for tf in tmp_files:
            tf.close()

def record_tmp_res(f=None,num=K,reverse=True):
    with open(f,'r') as f:
        count=collections.defaultdict(lambda:0)
        for i in f:
            count[i]+=1
        tmp=sorted(count.items(),lambda x,y:cmp(x[1],y[1]),reverse=reverse)
        tmp_res={}
        for i in range(num):
            tmp_res[tmp[i][0].strip()]=tmp[i][1]
        return tmp_res

def main():
    test_file='test.data'
    #create_data(test_file)
    devide_data(test_file)
    res={}
    for i in range(K):
        res.update(record_tmp_res(str(i)))
    tmp=sorted(res.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
    for i in range(K):
        print tmp[i]

if __name__=="__main__":
    main()
