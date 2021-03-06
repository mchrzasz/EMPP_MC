from ROOT import  * 
import sys

def main(argv=sys.argv):  


    pi=3.14159265359
    c=TCanvas("c1", "c1", 800,600)
 

    fun1=TF1("f2", "1.2732*(1-0.6366*x)", 0, pi/2) 
    fun1.SetLineColor(kBlue)             
    fun1.SetFillColor(1)                  
    fun1.SetTitle("")                     
    fun1.GetXaxis().SetTitle('x')         
    fun1.GetYaxis().SetTitle('y')         
                                     
    fun1.Draw()



    fun=TF1("f1", "0.9*cos(x)", 0, pi/2) 
    fun.SetLineColor(kBlack)             
    fun.SetFillColor(1)                  
    fun.SetTitle("")                     
    fun.GetXaxis().SetTitle('x')         
    fun.GetYaxis().SetTitle('y')         
    fun.Draw("SAME")  




    fun2=TF1("f3", "0.785*cos(x)/(1-2*x/3.1415)", 0, pi/2)
    fun2.SetLineColor(kRed)                        
    fun2.SetFillColor(1)                            
    fun2.SetTitle("")                               
    fun2.GetXaxis().SetTitle('x')                   
    fun2.GetYaxis().SetTitle('y')                   

    fun2.Draw("SAME")

    leg=TLegend(0.7, 0.6, 0.9, 0.8)
    leg.AddEntry(fun1, "g(x)", "L")
    leg.AddEntry(fun2, "w(x)", "L")
    leg.AddEntry(fun, "p(x)", "L")


    leg.Draw()
    c1.SaveAs("result.png")
        


if __name__ == "__main__":    
    sys.exit(main())      
