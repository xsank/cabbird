
def intToRoman(num):
    s=[]
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
    for i in range(length):
        while num>=dic[i][1]:
            s.append(dic[i][0])
            num-=dic[i][1]
    return ''.join(s)


if __name__=="__main__":
    print intToRoman(151)
    print intToRoman(1)
