#halfbandwidth computation for each matrix
#File:"q2chalfbandwidth"
n=4
def halfbandwidth(L):
    L=L
    
    n=rowdimension(L)
    y=[0]*n 
    yy=VerticalVector(y,n)
    hbandwidth=[0]*n
    b=[0]*n
    
    for j in range (n):
      
        for i in range (n):
            if (L[n-i-1][j]==0):
                hbandwidth[j]=hbandwidth[j]+1
            else:
                break
        
         
       
        
    for i in range (n):
        b[i]=n-i-hbandwidth[i]
    
    
    return  b




k=2*(n*n-n)+1
A=Incidence(n)
AT=Transpose(n*n-1,k,A)
Jk=[0]*k
Jk[k-1]=1 #dummy current source 
Jk=Matrix(Jk,k,1)
    
lefthandside=Multiplication(A,AT)
for z in range (n*n-1):
    for j in range (n*n-1):
        lefthandside[z][j]=lefthandside[z][j] / 10000
            
righthandside=Multiplication(A,Jk)
    
L=CholskeyL(lefthandside)

halfbandwidth=halfbandwidth(L)
halfbandwidth


SummaryHalfband=[0]*16

SummaryHalfband[2]=2 
SummaryHalfband[3]=4
SummaryHalfband[4]=5
SummaryHalfband[5]=6
SummaryHalfband[6]=7
SummaryHalfband[7]=8
SummaryHalfband[8]=9
SummaryHalfband[9]=10
SummaryHalfband[10]=11
SummaryHalfband[11]=12
SummaryHalfband[12]=13
SummaryHalfband[13]=14
SummaryHalfband[14]=15
SummaryHalfband[15]=16