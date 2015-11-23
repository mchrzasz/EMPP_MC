from ROOT import *
import math
import sys 

def main(argv=sys.argv):
    if(len(argv) != 4):
        print "Usage: python gen.py <a0> <ak> <k>"
        return -1
        
    a0=int(argv[1])
    ak=int(argv[2])
    k=int(argv[3])
    NTOYS=100
    for toy in range(0,NTOYS):
        for ik in range(0,NTOYS-k):
            
        


if __name__ == "__main__":      
    sys.exit(main())            


