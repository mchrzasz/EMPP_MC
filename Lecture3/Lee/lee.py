from ROOT import *            
import math                   
import sys                    
                              

def main(argv=sys.argv): 
    
    ran=TRandom3(132)
    NTOYS=1000000
    NBINS=50
    count_1bin=0
    count_lee=0
    for i in range(0, NTOYS):
        if( abs(ran.Gaus(0.,1.)) >3):count_1bin=count_1bin+1.
        for j in range(0,NBINS):
            if( abs(ran.Gaus(0.,1.)) >3): 
                count_lee=count_lee+1.
           #     print 'will break ', i, ' toy'
                break


    print '1 bin 3 sigma propability: ', count_1bin/NTOYS
    print '50 bins 3 sigma propability: ', count_lee/NTOYS

if __name__ == "__main__":    
    sys.exit(main())          
                              
