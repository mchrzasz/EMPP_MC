from ROOT import  * 
import sys
import numpy as np
from array import array


def main(argv=sys.argv):  

    ROOT.gStyle.SetOptFit()
    e=2.7182818284590452353602874713527
    seed=123
    rand = TRandom(seed)
    hist = TH1I("hist", "hist", 100,0.,100.)
    n_points=1000
    n_toys=[100, 1000, 10000, 100000]
    hists=[]
    
    for i in range(len(n_toys)):
        hists.append(TH1D('e with ' +str(n_toys[i]) +' toys', 'e with ' +str(n_toys[i]) +' toys' , 100, -3/sqrt(n_toys[i]),3/sqrt(n_toys[i])))
        
    for i_repear in range(n_points):
        for i in range(len(n_toys)):
            hist = TH1I("hist"+str(i), "hist", 100,0.,100.) 
            for itoy in range(0,n_toys[i]):
                n=0                     
                start=0.;               
                while(true):            
                    tmp=rand.Rndm()     
                    n=n+1               
                    if(tmp<start): break
                    else:               
                        start=tmp      
                       
                hist.Fill(n)          
            #print 'Measured e with ', n_toys[i], 'toys = ', hist.GetMean(), '+/- ', hist.GetMeanError()
            hists[i].Fill(hist.GetMean()-e)

    #############################################3
    c1= TCanvas("results", "results", 800,600)
    c1.Divide(2,2)
    sigma=[]
    sigma_err=[]
    for i in range(len(n_toys)): 
        c1.cd(i+1)
        hists[i].GetXaxis().SetTitle("#hat{e}-e")
        hists[i].Draw()
        hists[i].Fit("gaus")
        fit = hists[i].GetFunction("gaus");
        sigma.append(fit.GetParameter(2))
        sigma_err.append(fit.GetParError(2)) 

    c1.SaveAs("result_error.pdf")
    print sigma
    #############################################
    # Doing a graph error
    ############################################
    x=  np.array(n_toys)
    xe=np.array(n_toys)     
    for i in range(len(xe)):
        xe[i]=0.
    y= np.array(sigma)
    ye= np.array(sigma_err)
    print x,y,xe,ye
    print len(xe)
    gr=TGraphErrors(len(xe), array("d",x), array("d",y) ,array("d",xe) ,array("d",ye))
    gr.GetXaxis().SetTitle("N.of.Toys")
    gr.GetYaxis().SetTitle("Expected Uncertainty")
    
    c2=TCanvas("results_gr", "results_gr",  800,600)
    c2.cd()
    gr.Draw("AP")
    fun = TF1("fun","[0]/sqrt(x)",0.9*n_toys[0] ,1.1*n_toys[3])
    gr.Fit("fun")
    fun.Draw("SAME")
    c2.SetLogx();
    c2.SaveAs("result_error_dep.pdf")
    print 'Exiting'
    
if __name__ == "__main__":    
    sys.exit(main())      
