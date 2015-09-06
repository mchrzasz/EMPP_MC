from ROOT import  * 
import sys

def main(argv=sys.argv):
    ntoys=[10000,100000, 1000000, 10000000]
    for i in ntoys:
        calc_pi(i)

def calc_pi(NTOYS):

    # seting up dimensions
    L=1
    l=0.8
    pi=3.14159265359
    rand=TRandom3(12)
    # the lines on the table are at ..,-2L, -L, 0, L, 2L,...
    counter=0.
    
    
    
    for i in range(NTOYS):
        rand_y=rand.Rndm()-0.5 # this is in range (-0.5,0.5)
        rand_y=rand_y*2.*L # now we have range -L, L
        rand_angle=rand.Rndm()
        rand_angle=rand_angle*pi # this is the angle in range(0,pi)
        delta_y=(l/2)*cos(rand_angle)
        y_max=rand_y+abs(delta_y)
        y_min=rand_y-abs(delta_y) 
        if(y_max>L or y_min<-L): counter=counter+1. 
        if(y_max>0 and y_min<0): counter=counter+1.


    counter=counter/NTOYS
    #now remember P=2l/piL, so:
    Pi=2*l/(L*counter)
    counter_err=(1./sqrt(NTOYS))*sqrt(counter*(1.-counter))
    pi_err=(counter_err/counter)*Pi

    print NTOYS , round(Pi,5), round(Pi-pi,5), round(pi_err,5)



if __name__ == "__main__":    
    sys.exit(main())      
