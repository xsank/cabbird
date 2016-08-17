def getHint(secret, guess):
    bull_count=0
    cow_count=0
    secret_check=[]
    guess_check=[]
    for i,n in enumerate(secret):
        if n!=guess[i]:
            secret_check.append(n)
            guess_check.append(guess[i])
        else:
            bull_count+=1
    for n in guess_check:
        if n in secret_check:
            secret_check.remove(n)
            cow_count+=1
    return "%dA%dB" % (bull_count,cow_count)
    
    
if __name__=="__main__":
    print getHint("1807","7810")
    print getHint("1123","0111")
    print getHint("1122","2211")
    print getHint("1122","1222")