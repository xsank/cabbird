def memo(func):
    cache={}
    def decorate(*args):
        key=args
        if key not in cache:
            cache[key]=func(*args)
        return cache[key]
    return decorate


@memo
def lcs(sa,sb):
    if not (sa and sb):
        return ''
    if sa[-1]==sb[-1]:
        return ''.join([lcs(sa[:-1],sb[:-1]),sa[-1]])
    else:
        resb=lcs(sa,sb[:-1])
        resa=lcs(sa[:-1],sb)
        return resa if len(resa)>len(resb) else resb

if __name__=="__main__":
    print lcs('abcbdab','bdcaba')
