def isPrime(n):
    i=2
    while i*i<=n:
        if not n%i:
            return False
        i+=1
    return True

def countPrimes(n):
    total=0
    for i in range(2,n):
        if isPrime(i):
            total+=1
    return total
    

if __name__=="__main__":
    print countPrimes(10)
    print countPrimes(3)
    print countPrimes(2)
    print countPrimes(499979)
