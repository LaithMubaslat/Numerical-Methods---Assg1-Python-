#File:"q2cSparsityExcution
vterminal1= [0]*16
vterminal2= [0]*16#solution vector for different size 
from datetime import datetime
start_time=[0]*16
end_time=[0]*17
time=[0]*16
for i in range (2,16):
    start_time[i] = datetime.now()
    n=i
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
    y=Lybsparse(L,righthandside)
    x=LTxYSparse (L,y)
    firstterminal=n-1
    secondterminal=n*n-n
    vterminal1[i]=x[firstterminal][0]
    
    end_time[i] = datetime.now()
    time[i]=end_time[i]-start_time[i]
    
    
    
    
Sourcevoltagedifference= [0]*16
RnetSparse=[0] *16
for i in range (2,16):
    Sourcevoltagedifference[i]=vterminal1[i]
    RnetSparse[i]=10000*Sourcevoltagedifference[i]/(10000-Sourcevoltagedifference[i])