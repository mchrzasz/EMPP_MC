from ROOT import *
import math
import sys 

def main(argv=sys.argv):
    if(len(argv) != 3):
        print "Usage: python gen.py <X0> <m>"
        return -1
        
    X0=int(argv[1])
    m=int(argv[2])
    NTOYS=100
    tmp=X0**2
    R_numbers=[]
    R_numbers.append(X0)
    for i in range(NTOYS):
        
        r1,c1 = math.modf(tmp*10**(-m))
        r2,c2=  math.modf(tmp*10**(-3*m))
        X0=c1-c2
        R_numbers.append(X0) 
        tmp=X0**2
        print X0

    print R_numbers


if __name__ == "__main__":      
    sys.exit(main())            


