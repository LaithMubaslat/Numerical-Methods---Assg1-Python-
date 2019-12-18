
#CholskeyCode

def CholskeyL(A):
    
    #1st step: Check if A is square
    
    if(rowdimension(A)!=columndimension(A)):
        print ("matrix not square; Cholskey Decomp. Not Possible")
        return  
    
    
    n=rowdimension(A)
    zeros=[0] * (n*n)
    L=Matrix(zeros,n,n)

    
    
    
    for j in range (n):
        for i in range (j,n) :  
            if (i==j):
                
                #will have to add something here as j increases
                L[j][j]=sqrt(A[j][j])
                
                
              
            if(i!=j):
                L[i][j]=A[i][j]/L[j][j]
                for k in range (j+1,i+1):
                    A[i][k]=A[i][k]-L[i][j]*L[k][j]
                    
            if(i==(j+1)):
                A[j][j]=A[j][j]-L[i][j]*L[i][j]
    
          
    
   
            
    return L
        