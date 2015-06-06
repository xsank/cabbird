
def addBinary(a, b):
    return bin(int(a,2)+int(b,2))[2:]


if __name__=="__main__":
    print addBinary('11','1')
