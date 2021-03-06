from ROOT import  * 
import sys

def main(argv=sys.argv):  


    pi=3.14159265359
    c=TCanvas("c1", "c1", 800,600)
    fun=TF1("f1", "0.9*cos(x)", 0, pi/2)
    fun.SetLineColor(kBlack)
    fun.SetFillColor(1)
    fun.SetTitle("")
    fun.GetXaxis().SetTitle('x')  
    fun.GetYaxis().SetTitle('y')

    fun.Draw("FC")

    c1.SaveAs("result.png")
        


if __name__ == "__main__":    
    sys.exit(main())      
