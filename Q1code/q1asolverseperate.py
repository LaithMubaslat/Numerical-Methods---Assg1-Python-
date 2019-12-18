
#Solver y from L and b > x from y and LT File:"SolverSeperate.py"

def Lyb(L,b):
    L=L
    b=b
    n=rowdimension(L)
    y=[0]*n 
    yy=VerticalVector(y,n)
    
    
    for i in range (n):
        sum=0
        for j in range (i):
            sum=sum+L[i][j]*yy[j][0]
         
       
        yy[i][0]=(b[i][0]-sum)/L[i][i]
    
    
    
    return yy




def LTxY (L,yy):
    n=rowdimension(L)
    LT=Transpose(n,n,L)
    x=[0]*n 
    xx=VerticalVector(x,n)
    
    for i in range (n):
        counter=n-i-1
        sum=0
        for k in range (i):
            sum=sum+LT[counter][counter+k+1]*xx[counter+k+1][0]
            
        xx[counter][0]=(yy[counter][0]-sum)/LT[counter][counter]
    
    
    return xx


    