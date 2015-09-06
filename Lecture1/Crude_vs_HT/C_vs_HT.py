from ROOT import  *
import sys
from array import array
###############################################
# Example of program to calculate ingerals    #
# with crude and Heads and Tails method       #
###############################################

def main(argv=sys.argv):

    ROOT.gStyle.SetOptFit()
    pi=3.14159265359
    nexriments=1000 # not more than 3000 please
    ntoys=[100,1000,10000, 100000]
    seed=100
    x=[]
    xe=[]
    y_HT=[]
    y_C=[]
    ye_HT=[] 
    ye_C=[]  
    hists_HT=[]
    hists_C=[]

    for i in ntoys:
        hists_HT.append(TH1F("HT_"+str(i), "HT_"+str(i), 100, 1.- 3.5/sqrt(i), 1.+ 3.5/sqrt(i)))
        hists_C.append(TH1F("C_"+str(i), "C_"+str(i), 100, 1.- 3.5/sqrt(i), 1.+ 3.5/sqrt(i)))
        x.append(i)
        xe.append(0.)
    for j in range(nexriments):

        for i in range(len(ntoys)):
            int_HT= calc_integral_HT(ntoys[i],0,pi/2,seed,1.)
            int_C=calc_integral_Crude(ntoys[i],0,pi/2,seed)
            seed+=1
            hists_HT[i].Fill(int_HT)
            hists_C[i].Fill(int_C)
            #print int_HT, int_C
    #plotting stuff, no fun here, you can ignore if you do not like code
    c1= TCanvas("c1", "c1", 800,600)
    c1.Divide(2,2)
    c1.cd(1)
    hists_HT[0].Draw()
    hists_HT[0].Fit("gaus")
    fit = hists_HT[0].GetFunction("gaus") 
    y_HT.append(fit.GetParameter(2))
    ye_HT.append(fit.GetParError(2))
    c1.cd(2)
    hists_C[0].Draw()
    hists_C[0].Fit("gaus")
    fit = hists_C[0].GetFunction("gaus")
    y_C.append(fit.GetParameter(2))     
    ye_C.append(fit.GetParError(2))     
    c1.cd(3)
    hists_HT[1].Draw()
    hists_HT[1].Fit("gaus")
    fit = hists_HT[1].GetFunction("gaus") 
    y_HT.append(fit.GetParameter(2))      
    ye_HT.append(fit.GetParError(2))      
    c1.cd(4)
    hists_C[1].Draw()
    hists_C[1].Fit("gaus")
    fit = hists_C[1].GetFunction("gaus")
    y_C.append(fit.GetParameter(2))     
    ye_C.append(fit.GetParError(2))     

    c1.SaveAs("results_0.pdf")

    c1.cd(1)
    hists_HT[2].Draw()
    hists_HT[2].Fit("gaus")
    fit = hists_HT[2].GetFunction("gaus")
    y_HT.append(fit.GetParameter(2))     
    ye_HT.append(fit.GetParError(2))     

    c1.cd(2)
    hists_C[2].Draw()
    hists_C[2].Fit("gaus")
    fit = hists_C[2].GetFunction("gaus") 
    y_C.append(fit.GetParameter(2))      
    ye_C.append(fit.GetParError(2))      

    c1.cd(3)
    hists_HT[3].Draw()
    hists_HT[3].Fit("gaus")
    fit = hists_HT[3].GetFunction("gaus")
    y_HT.append(fit.GetParameter(2))     
    ye_HT.append(fit.GetParError(2))     

    c1.cd(4)
    hists_C[3].Draw()
    hists_C[3].Fit("gaus")
    fit = hists_C[3].GetFunction("gaus")
    y_C.append(fit.GetParameter(2))     
    ye_C.append(fit.GetParError(2))     

    c1.SaveAs("results_1.pdf")

    # making 2 TGraph errors
    gr_HT=TGraphErrors(len(xe), array("d",x), array("d",y_HT) ,array("d",xe) ,array("d",ye_HT))      
    gr_C=TGraphErrors(len(xe), array("d",x), array("d",y_C) ,array("d",xe) ,array("d",ye_C))
    
    c3=TCanvas("c3", "c3", 600,500)
    c3.SetLogx();

    gr_HT.Draw("AP")
    fun = TF1("fun","[0]/sqrt(x)",0.9*ntoys[0] ,1.1*ntoys[3])
    gr_HT.Fit("fun")

    c3.SaveAs("results_fit_0.pdf") 


    gr_C.Draw("AP") 
    fun1 = TF1("fun1","[0]/sqrt(x)",0.9*ntoys[0] ,1.1*ntoys[3])
    gr_C.Fit("fun1")
    c3.SaveAs("results_fit_1.pdf")
    

    ##############################
    
    
    
# let's be simple and calculate integral  of cos(x)
def fun(x):
    return cos(x)


def calc_integral_HT(NTOYS, x_min, x_max,seed, y_max):

    # seting up dimensions
    rand=TRandom3(seed)
    # the lines on the table are at ..,-2L, -L, 0, L, 2L,...

    counter=0.
    for i in range(NTOYS):
        x=rand.Rndm()
        x=x*(x_max-x_min)+x_min
        y=rand.Rndm()*y_max
        if(y<fun(x)): counter=counter+1.

    integral=(counter/NTOYS)*(x_max-x_min)*y_max
    return integral

def calc_integral_Crude(NTOYS, x_min, x_max,seed):
    rand=TRandom3(seed)

    counter=0.
    for i in range(NTOYS):
        x=rand.Rndm()
        x=x*(x_max-x_min)+x_min
        counter+=fun(x)
    integral=counter/NTOYS*(x_max-x_min)
    return integral

if __name__ == "__main__":
    sys.exit(main())
