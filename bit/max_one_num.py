
def count_max_one(num=0):
    sum=0
    n=num
    while n:
        n&=n-1
        sum+=1
    return sum

