
def titleToNumber(s):
    sum=0
    for c in s:
        sum=sum*26+(ord(c)-64)
    return sum


if __name__=="__main__":
    print titleToNumber('AA')
    print titleToNumber('A')

