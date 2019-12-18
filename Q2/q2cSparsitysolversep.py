
#lookahead ra8am 3 
#File:"q2cSparsitysolversep.py"
from math import sqrt
def Lybsparse(L,b):
    L=L
    b=b
    n=rowdimension(L)
    y=[0]*n 
    yy=VerticalVector(y,n)
    
    halfbandwidth=int(sqrt(n+1))+1
    z=0
    for i in range (n):
        sum=0
        if (i==halfbandwidth):
            z=z+1
    
        for j in range (z,i):
            sum=sum+L[i][j]*yy[j][0]
         
       
        yy[i][0]=(b[i][0]-sum)/L[i][i]
        
    
    
    
    return yy


Lybsparse(L,righthandside)
Lyb(L,righthandside)

def LTxYSparse (L,yy):
    n=rowdimension(L)
    LT=Transpose(n,n,L)
    x=[0]*n 
    xx=VerticalVector(x,n)
    halfbandwidth=int(sqrt(n+1))+1
    z=0
    for i in range (n):
        counter=n-i-1
        sum=0
        if (i==halfbandwidth):
            z=z+1
        for k in range (i-z):
            sum=sum+LT[counter][counter+k+1]*xx[counter+k+1][0]
            
        xx[counter][0]=(yy[counter][0]-sum)/LT[counter][counter]
    
    
    return xx
