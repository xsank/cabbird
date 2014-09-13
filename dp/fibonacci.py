
def memo(func):
    cache={}
    def wrap(n):
        if n not in cache:
            cache[n]=func(n)
        return cache[n]
    return wrap

@memo
def fib(i):
    return 1 if i < 2 else fib(i-1)+fib(i-2)

if __name__=="__main__":
    print fib(100)
