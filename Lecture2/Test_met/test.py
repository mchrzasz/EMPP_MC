from ROOT import *            
import math                   
import sys                    
                              

def main(argv=sys.argv): 
    if(len(argv)!=5):
       print 'Usage, python test.py <mean> <sigma> <NTOYS> <NOPINTS>'
       return -1
    
    ran=TRandom3(132)
    mean=float(argv[1])
    sigma=float(argv[2])
    NTOYS=int(argv[3])
    NPOINTS=int(argv[4])
    hist_mean=TH1F("mean estimator, true value="+str(mean), "mean estimator, true value="+str(mean),300,  mean-5*sigma, mean+5*sigma) 
       
    for i in range(0,NTOYS):
       # simulating ith toy
       points=[]
       for j in range(0,NPOINTS):
          points.append(ran.Gaus(mean, sigma))
       # we finished ith toy, let's estimate the mean of a gauss
       mean_tmp= reduce(lambda x, y: x + y, points) / len(points)
       
       hist_mean.Fill(mean_tmp)
    c1=TCanvas("c1", "c1", 800,600)
    hist_mean.Draw()
    c1.SaveAs("mean_estimator.png")
       

if __name__ == "__main__":    
    sys.exit(main())          
                              
