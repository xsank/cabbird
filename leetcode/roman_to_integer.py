
def romanToInt(s):
    dic=[
        ("M",1000),
        ("CM",900),
        ("D",500),
        ("CD",400),
        ("C",100),
        ("XC",90),
        ("L",50),
        ("XL",40),
        ("X",10),
        ("IX",9),
        ("V",5),
        ("IV",4),
        ("I",1)
    ]
    length=len(dic)
    sum=0
    index=0
    for i in range(length):
        while s[index:].startswith(dic[i][0]):
            sum+=dic[i][1]
            index+=len(dic[i][0])
    return sum

if __name__=="__main__":
    print romanToInt("I")
    print romanToInt("CLI")
    print romanToInt("MCMXCVI")
