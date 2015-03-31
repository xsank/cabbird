
def hammingWeight(n):
    count=0
    while n:
        count+=1
        n&=n-1
    return count


if __name__=="__main__":
    print hammingWeight(3)
