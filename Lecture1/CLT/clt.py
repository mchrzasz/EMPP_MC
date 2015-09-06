from ROOT import  * 
import sys

def main(argv=sys.argv):  


    pi=3.14159265359
    c=TCanvas("c1", "c1", 800,600)
 
    NTOYS=1000000
    rand=TRandom(123)    

    hists=[]

    for i in range(1,13, 2):
        hist=TH1D("hist", "hist", 400, 0, 10)
        for j in range(0, NTOYS):
            tmp=0.
            for k in range(0,i):
                tmp+=rand.Rndm()
            hist.Fill(tmp)
        hists.append(hist)

    for i in range(0,len(hists)): 
        if(i==0): hists[i].DrawNormalized()
        else: hists[i].DrawNormalized("SAME")

    c.SaveAs("clt.png")
    c.SaveAs("clt.pdf")  
if __name__ == "__main__":    
    sys.exit(main())      
