#File:"Q2A-Incidence.py"

n=4

def Incidence(N):

    n=N
    columns= (2*(n*n-n))
    columns=columns+1 #column added for dummy source current
    rows= n*n
    numberofelements=rows*columns
    Vector = [0] *( numberofelements )


    A=Matrix(Vector, rows, columns)

    i=0
    x=0
    currentcounter=0
    counteri=0
    for i in range (0,n*(n-1)): 

        if ((i)%(n-1)==0 and i !=0 ): 
            x=x+1

        
  
        count=0
        alpha=i+x
        beta=i+x+2
        for j in range (alpha,beta): 
            count=count+1  
            if (count%2==0):
                A[j][i]=-1
            else: A[j][i]=+1
        
    
        counteri=counteri+1
  


    for i in range (0,n*(n-1)): 
    
        j1= i 
        j2= i+n
    
        A[j1][counteri]=+1
        A[j2][counteri]=-1 
        counteri=counteri+1
    
    
    import numpy as np


    #Source Current Values 

    A[n-1][columns-1]=+1 
    A[n*n-n][columns-1]=-1
    A0=np.array(A)



#remove the last line to obtain the reduced incidence matrix / the removed node ..
#is that of one of the terminals of which we want measure the resistance from 
    Ar=[0]* ((rows-1)*columns)
    Ar=Matrix(Ar,rows-1,columns)
    for i in range (n*n-n):
        for j in range (columns):
            Ar[i][j]=A[i][j]
            
    for i in range (n*n-n+1,rows):
        for j in range (columns):
            Ar[i-1][j]=A[i][j]
            
    
    
    return Ar

