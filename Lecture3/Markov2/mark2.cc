#include "TF1.h"
#include "TCanvas.h"
#include "TApplication.h"
#include "TH3D.h"
#include "TH2D.h"
#include "TRandom.h"
#include "TRandom3.h"
#include "TMath.h"
#include <cmath>
#include <iostream>
#include <cstdio>
#include "TStyle.h"

#include<cstdlib>


using namespace std;

void solution(double &x,double &y,double &z,int traj, TRandom *gen)
{
  //double p[3]={0.9,0.8,0.7};
   double p[3]={0.3,0.3,0.6};
  double hPrim[3][3]={{0.3,0.5,0.9},{0.3,0.6,0.9},{0.6,0.7,0.9}};
  //double hPrim[3][3]={{0.9,1,1},{0.8,0.8,1},{0.7,0.7,0.7}};
  
  double a[3]={1.5, -1.,0.7};
  double wynik[3]={0.,0.,0.};
  double ran;
  double q[3]={1./3.,1./3.,1./3.};
  int i,ik;
  int n;
  ik=0;
  for(int j=0;j<traj;++j)
    {
      ran=gen->Rndm();
      if(ran<=q[0]){n=0;}
      if(ran>q[0] && ran<q[0]+q[1]){n=1;}
      if(ran>q[0]+q[1]){n=2;}
      i=n+1;
      while(i!=0)
	{
	  ran=gen->Rndm();
	  //if(n==2){cout<<i<<" ran="<<ran<<" ";}
	  if(hPrim[i-1][0]>ran){ik=i; i=0;}
	  else
	    {
	      for(int m=2;m>=0;--m)
		{
		  if(hPrim[i-1][m]<ran)
		    {
		      ik=i;
		      i=m+1;
		      break;
		    }
		}
	    }
	}

      // if(n==2){cout<<endl;}

      wynik[ik-1]+=a[n]/(p[ik-1]*q[n]);
    }
  x=wynik[0]/(double)traj;
  y=wynik[1]/(double)traj;
  z=wynik[2]/(double)traj;
}

int main(int argc, char ** argv){
  
  if(argc !=2) return -1;
  int NTOYS= atoi(argv[1]);
  
  gStyle->SetOptFit(1);
  gStyle->SetTitleFillColor(0);
  gStyle->SetStatColor(0);
  double x,y,z;
  TRandom *gen=new TRandom3();
  solution(x,y,z, NTOYS,gen);
  cout<<x<<" "<<y<<" "<<z<<endl;
return 0;
}

