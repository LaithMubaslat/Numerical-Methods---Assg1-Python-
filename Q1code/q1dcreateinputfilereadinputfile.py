#q1d create input file / read input file 
#File:"q1dcreateinputfilereadinputfile.py"

def SaveNetworkMatricesAsText(networkname,JK,RK,EK,A,n,k): 
    
    name= networkname
    f= open(name,"w+") #creates a network file
   
    f.write("Network Name: %s \r\n JK,RK,EK and reduced A Matrix Parameters \r\n" %networkname)
    f.write("number of nodes:\r\n")
    f.write("%d;\r\n" %(n) )
    f.write("number of branches\r\n")
    f.write("%d;\r\n" %(k) )#write parameters of the 4 matrices to be used in code
    
    #first matrix saved is A; comma seperated; 1 line 
    
    #2nd matrix JK 
    f.write("Jk Rk Ek\r\n" )
    for i in range(k):       
        a=JK[i][0]
        b=RK[i][0]
        c=EK[i][0]
        f.write("%f,%f,%f;\r\n" % (a,b,c))
            
            

    
    f.write("A\r\n" )
    for i in range(n-1):
        for j in range (k):
            if j!=(k-1):
                f.write("%f," % A[i][j])
            else:
                f.write("%f" % A[i][j])
            
             
        f.write(";\r\n" )  
        
        
    
    f.write("E" )  

def ReadMatrices(string): 
    
    f= open(string) #creates a network file
   
    lines=f.readlines()
    


    

    
    i=0
    while lines[3][i]!=';':
        i=i+1
    
    n=int(lines[3][0:i])
    
    i=0
    while lines[5][i] !=';':
        i=i+1
    
    k=int(lines[5][0:i])
    
    
    Jk=[0]*k
    Ek=[0]*k
    Rk=[0]*k
    A=[0]*(k*(n-1))
    
    
    
    
    
    for i in range (k): 
        j=0
        #writes down Jk elements 
        counter1=0
        while lines[7+i][j]!=',':
            counter1=counter1+1 
            j=j+1
        sumcounter=counter1
        Jk[i]=float(lines[7+i][sumcounter-counter1+1*0:sumcounter])
        j=j+1
        
        
        
        #writes down Rk elements 
        counter2=0
        while lines[7+i][j]!=',':    
            counter2=counter2+1 
            j=j+1
        
        
        sumcounter=sumcounter+counter2
        Rk[i]=float(lines[7+i][sumcounter-counter2+1*1:sumcounter])
        j=j+1
        
            
        ##writes down Ek elements 
        counter3=0
        while lines[7+i][j]!=';' :  
            counter3=counter3+1
            j=j+1
        sumcounter=sumcounter+counter3    
        Ek[i]=float(lines[7+i][sumcounter-counter3+1*2:sumcounter]   )
        
     
        
        
    #A will start from 7+k+1 
    #have to account for negative elements in A 
    element=0
    for i in range (k+8,n+k+8): 
        
        if (lines[i][0]=='E'):
            break
        
        sumcounter=0
        counter=[0]*k 
        j=0
        for z in range (k): 
            
            while (lines[i][j]!=',' ):
                counter[z]=counter[z]+1 
                j=j+1
                if (lines[i][j]==';'):
                    break
            
            j=j+1
            sumcounter=sumcounter+counter[z]
            
            
        
            A[element]=float(lines[i][sumcounter-counter[z]+1*z:sumcounter])
       
            element=element+1
        
        
            if (element==k):
                break
        
        
    
    
    A=Matrix(A,n-1,k)
    JK=Matrix(Jk,k,1)
    EK=Matrix(Ek,k,1)
    RK=Matrix(Rk,k,1)
    
    return {'A':A, 'JK':JK ,'RK':RK,'EK':EK, 'n':n, 'k':k }
    