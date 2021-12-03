K = [2,5,7,11,13,17,19,23]

U = 72


def verifier(k:int,a:int,b:int,c:int,A:int,B:int,D:int,E:int)->bool :
    eq1:bool = (a**(2*k))%72 == c**(2*k)
    
    eq2:bool = (c**k + b**k)%72 == A**k
    
    eq3:bool = (b**k + D**k)%72 == c**k
    
    eq4, eq5 = b%8 == 0, b%3 == 0
    
    eq6:bool = (a**2)%72 == A*D
    
    eq7:bool = (c**k - a**k)%72 == (E**k)/2
    
    eq8:bool = (c**k + a**k)%72 == 2*(B**k)
    
    eq9:bool = (b**2)%72 == B*E
    
    return (eq1 and eq2 and eq3 and eq4 and eq5 and eq6 and eq7 and eq8 and eq9)


for k in K:
    print(f"Les solutions pour k = {k}")
    for a in range(U):
        for b in range(U):
            for c in range(U):
                for A in range(U):
                    for B in range(U):
                        for D in range(U):
                            for E in range(U):
                                if verifier(k,a,b,c,A,B,D,E):
                                    print(f"k = {k}, a = {a}, b = {b}, c = {c}, A = {A}, B = {B}, D = {D}, E = {E}")