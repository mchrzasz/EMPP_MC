from ROOT import  * 
import sys

def main(argv=sys.argv):  
    e=2.7182818284590452353602874713527
    seed=123
    rand = TRandom(seed)
    hist = TH1I("hist", "hist", 100,0.,100.)
    for i in range(1,10**8+1):
        n=0
        start=0.;
        while(true):
            tmp=rand.Rndm()
            n=n+1
            if(tmp<start): break
            else:

                start=tmp
        hist.Fill(n)
        if( (i ==100) or (i==10000) or (i==1000000) or (i==10**8)):
            print round(hist.GetMean(), 6), round(hist.GetMean()-e, 6)
        


if __name__ == "__main__":    
    sys.exit(main())      
