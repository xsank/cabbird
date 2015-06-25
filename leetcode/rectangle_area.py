
def computeArea(A, B, C, D, E, F, G, H):
    _A=max(A,E)
    _B=max(B,F)
    _C=min(C,G)
    _D=min(D,H)
    _SIZE=0 if _A>=_C or _B>=_D else (_C-_A)*(_D-_B)
    return (C-A)*(D-B)+(G-E)*(H-F)-_SIZE


if __name__=="__main__":
    print computeArea(-3,0,3,4,0,-1,9,2)
