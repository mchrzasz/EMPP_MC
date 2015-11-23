#include <cmath>
#include<iostream>
#include <stdio.h>
#include <stdlib.h>
#include <TRandom1.h>


using namespace std;

int main(int argc, char **argv)
{
  double h[3][4]={ {0.4, 0.2, 0.3,0.1},{0.1,0.4,0.3,0.2},{0.5,0.3,0.1,0.1}};
  double a[3]={1.5,-1.0,0.7};
  int j = atoi(argv[1]);
  int original =j;
  int n_of_samples = atoi(argv[2]);
  TRandom1 *rand =  new TRandom1(2131);
  double result =0;
  double result2=0;
  for(int i =0;i< n_of_samples;++i)
    {
      int last;
      j=original;
      while(1)
	{
	  last =j;
	  double tmp =rand->Rndm();
	  if(tmp<h[j-1][0]) j=0;
	  else if(tmp > h[j-1][0] && tmp<h[j-1][1]+h[j-1][0]) j=1;
	  else if(tmp > h[j-1][1]+h[j-1][0] && tmp<h[j-1][2]+h[j-1][1]+h[j-1][0]) j=2;    
	  else if(tmp > h[j-1][2]+h[j-1][1]+h[j-1][0] && tmp<h[j-1][3]+h[j-1][2]+h[j-1][1]+h[j-1][0]) j=3;     
	  else
	    {
	      cout<<"rand= "<<tmp<<endl;
	      cout<<h[j-1][3]+h[j-1][2]+h[j-1][1]+h[j-1][0]<<endl;
	    }
	  if(j==0) break;
      
	}
      
      result+=a[last-1]/(double)(h[last-1][0]);
      //errors
    
    }

  cout<<result/ n_of_samples<<endl;


  return 1;
}
