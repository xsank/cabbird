
def count_max_one(num=0):
    sum=0
    while num:
        num&=num-1
        sum+=1
    return sum

