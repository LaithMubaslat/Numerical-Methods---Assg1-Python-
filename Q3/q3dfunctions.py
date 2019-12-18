


def Jacobisolve(Vk1,Vk2,deltax,deltay,alpha,beta, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection):
    
    
    
    
    for i in range (1,bottomleftedgeXnode):
        for j in range (1,bottomleftedgeYnode):
            alpha1=alpha[i-1]
            alpha2=alpha[i]
            beta1=beta[j-1]
            beta2=beta[j]
        
        
        #first term
            term1=deltax*deltax
            term1=term1*deltay*deltay
            term1=term1*alpha1*alpha2*beta1*beta2
            term1=term1/2
            term1=term1/(beta1*beta2*deltay*deltay+alpha1*alpha2*deltax*deltax)
        
        
        #second term
            term2=deltax*deltax*alpha1*alpha2*(alpha1+alpha2)
            term2=2/term2
        
        #third term 
            term3=deltay*deltay*beta1*beta2*(beta1+beta2)
            term3=2/term3 
        
        
        
        
        
        #change2 to 1 (mn el jehatein entabih)
            Vk2[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk2[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk2[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk2[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk2[i][j]= term1 *             Vk1[i][j]
        
        #vk1[i][j-1] vk1[i-1][j] will have been computed for k+1 to be used in computing vk1[i][j]
            
        for j in range (bottomleftedgeYnode,nodesxdirection-1):
            
            alpha1=alpha[i-1]
            alpha2=alpha[i]
            beta1=beta[j-1]
            beta2=beta[j]
        
        
        #first term
            term1=deltax*deltax
            term1=term1*deltay*deltay
            term1=term1*alpha1*alpha2*beta1*beta2
            term1=term1/2
            term1=term1/(beta1*beta2*deltay*deltay+alpha1*alpha2*deltax*deltax)
        
        
        #second term
            term2=deltax*deltax*alpha1*alpha2*(alpha1+alpha2)
            term2=2/term2
        
        #third term 
            term3=deltay*deltay*beta1*beta2*(beta1+beta2)
            term3=2/term3 
        
        
        
        
        
        #change2 to 1 (mn el jehatein entabih)
            Vk2[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk2[i][j]=  (term2 * alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk2[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk2[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk2[i][j]= term1 *             Vk1[i][j]
        
            
        
            
        #boundary/beta1 term is removed 
        j=nodesydirection-1
        alpha1=alpha[i-1]
        alpha2=alpha[i]
        
        beta1=beta[j-1]
        beta2=beta1 
        
        
        
        #first term
        term1=deltax*deltax
        term1=term1*deltay*deltay
        term1=term1*alpha1*alpha2*beta1*beta2
        term1=term1/2
        term1=term1/(beta1*beta2*deltay*deltay+alpha1*alpha2*deltax*deltax)
        
        
        #second term
        term2=deltax*deltax*alpha1*alpha2*(alpha1+alpha2)
        term2=2/term2
        
        #third term 
        term3=deltay*deltay*beta1*beta2*(beta1+beta2)
        term3=2/term3 
        
        
        
        
        #vk[i][j+1] replaced with vk[i][j-1] and beta2 is used instead of beta1 considering how 
        #these parameters are equal due to mirror symmetry
        #change2 to 1 (mn el jehatein entabih)
        Vk2[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
        Vk2[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
        Vk2[i][j]= (term3 * beta1 * Vk1[i][j-1]) +               Vk1[i][j]
        Vk2[i][j]= (term3*beta1 * Vk1[i][j-1]) +                Vk1[i][j]
        Vk2[i][j]= term1 *             Vk1[i][j]
        
            
        
        
        
    for i in range (bottomleftedgeXnode,nodesxdirection-1):
        for j in range (1,bottomleftedgeYnode):
            alpha1=alpha[i-1]
            alpha2=alpha[i]
            beta1=beta[j-1]
            beta2=beta[j]
        
        
        #first term
            term1=deltax*deltax
            term1=term1*deltay*deltay
            term1=term1*alpha1*alpha2*beta1*beta2
            term1=term1/2
            term1=term1/(beta1*beta2*deltay*deltay+alpha1*alpha2*deltax*deltax)
        
        
        #second term
            term2=deltax*deltax*alpha1*alpha2*(alpha1+alpha2)
            term2=2/term2
        
        #third term 
            term3=deltay*deltay*beta1*beta2*(beta1+beta2)
            term3=2/term3 
        
        
        
        
        
        #change2 to 1 (mn el jehatein entabih)
            Vk2[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk2[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk2[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk2[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk2[i][j]= term1 *             Vk1[i][j]
        
            
                
    for j in range (1,bottomleftedgeYnode):             
        i=nodesxdirection-1
        #alpha1 removed
        alpha1=alpha[i-1]
        alpha2=alpha1
        beta1=beta[j-1]
        beta2=beta[j]
        #first term
        term1=deltax*deltax
        term1=term1*deltay*deltay
        term1=term1*alpha1*alpha2*beta1*beta2
        term1=term1/2
        term1=term1/(beta1*beta2*deltay*deltay+alpha1*alpha2*deltax*deltax)
        #second term
        term2=deltax*deltax*alpha1*alpha2*(alpha1+alpha2)
        term2=2/term2
        #third term
        term3=deltay*deltay*beta1*beta2*(beta1+beta2)
        term3=2/term3 
     
     
     
        #vk[i+1][j] and alpha2 replaced with vk[i-1][j] and alpha1 since semetry
        #change2 to 1 mn el jehatein entabih   
        Vk2[i][j]= (term2 * alpha1 * Vk1[i-1][j]) 
        Vk2[i][j]=  (term2 * alpha1 * Vk1[i-1][j] )          + Vk1[i][j]
        Vk2[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
        Vk2[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
        Vk2[i][j]= term1 *             Vk1[i][j]
        
            
    return Vk2



         
                


def jacobisolution(point,T,w,deltax,deltay, equalspacing, xydimension,Vinnerouter,centercond,alpha,beta ): 
    
    
    
    #inner conudctor location 
    center=[xydimension[0]/2,xydimension[1]/2]
    #deltaxanddeltay
    if equalspacing==1:
        deltax=h
        deltay=h
        
    
    edgex=(xydimension[0]/2)-centercond[1]/2
    
    
    
    
    edgey=(xydimension[1]/2-centercond[0]/2)
    
    
    
    
    point[0] 
    
    
    point[1] 
    
    
    pointcoordinateXcheck=0
    pointcoordinateYcheck=0
    
    
    equalspacing=1
    
    #check validity of alpha/beta values 
    
 
        

    #numberofnodes/constant(for both equal and unequal)because the assignment requires an equal number of nodes even in the case of unequal spacing 
    if equalspacing==1: 
        nodesxdirection = int((xydimension[0]/(2*deltax) + 1)) #perline
        nodesydirection = int(xydimension[1]/(2*deltay)+1) #perline
        n=nodesxdirection* nodesydirection #total number of nodes
        n=int(n)
        numberofalphas=nodesxdirection-1
        numberofbetas=nodesydirection-1
        alpha=[1]*(numberofalphas)
        beta=[1]*(numberofbetas)
        bottomleftedgeXnode=edgex/deltax
        bottomleftedgeYnode=edgey/deltay
        outpointx=int(point[0]/h)
        outpointy=int(point[1]/h)
        
        if int(point[0]/h)!=outpointx:
            print ("h not appropriate for including output point x coordinate. choose a different value for deltax/h ")
            return
        
        if int(point[1]/h)!=outpointy:
            print ("h not appropriate for including output point y coordinate. choose a different value for deltay/h ")
            return
        
            
        if int(bottomleftedgeXnode)!=bottomleftedgeXnode:
            print ("h not appropriate for assigning nodes to edges. choose a different value for deltax/h ")
            return
    
        bottomleftedgeXnode=int(bottomleftedgeXnode)   
        
        
        if int(bottomleftedgeYnode)!=bottomleftedgeYnode:
            print ("h not appropriate for assigning nodes to edges. choose a different value for deltay/h ")
            return
        
        if h>xydimension[0] or h>xydimension[1]:
            print ("h not appropriate for problem geometry")
            return
    
        bottomleftedgeYnode=int(bottomleftedgeYnode)

    
    
        
        

    #define nodes 
    
    
    
    voltagevector=[0]*(n)   #symmetry exploited here
    Voltage0=Matrix(voltagevector,nodesxdirection,nodesydirection)      #symmetry exploited here
    Voltage1=Matrix(voltagevector,nodesxdirection,nodesydirection) 
    Voltage2=Matrix(voltagevector,nodesxdirection,nodesydirection) 
    R=Matrix(voltagevector,nodesxdirection,nodesydirection) 
    
    ############################################################################
    
    
    
        #lhon
   
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    #flag for inappropriate deltax/deltay/h choice : problem geometry specific 
    
    
    
    
    
    

    
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    
    #Setting initial voltage values / problem geometry specific 
    
    for i in range (nodesxdirection): 
        Voltage0 [0][i]= Vinnerouter[1]   #bottom 0v conductor /symmetry exploited
        Voltage0 [i][0]= Vinnerouter[1]   #left 0v conductor / symmetry exploted 
        Voltage1 [0][i]= Vinnerouter[1]   #bottom 0v conductor /symmetry exploited
        Voltage1 [i][0]= Vinnerouter[1]
        Voltage2 [0][i]= Vinnerouter[1]   #bottom 0v conductor /symmetry exploited
        Voltage2 [i][0]= Vinnerouter[1]
        
    
    
    #center conductor voltages
    for i in range (bottomleftedgeXnode,nodesxdirection):
        for j in range (bottomleftedgeYnode,nodesydirection):
            Voltage0 [i][j]=Vinnerouter[0]  
            Voltage1 [i][j]=Vinnerouter[0]  
            Voltage2 [i][j]=Vinnerouter[0]  
         
    
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    ############################################################################
    #numerical solution
    
    ############################################################################
    #step1 make a guess 
    #let the guess be zeros which is already there 
    
    
    #for statement begins here 
    ############################################################################
    #compute gaus seidel method values at iteration k+1 
    #make a copy of voltage vector 
    Vk0=Voltage0 #k
    Vk1=Voltage1 # after gauss
    Vk2=Voltage2 #k+1 after SOR
    #equationterms:
    #terms matrices in terms of alpha and beta 
    
    outputpoint=[outpointx,outpointy]
    
    #7ot equation gauss hon 
    
    true=1
    i=0
    #newgaussfile
    counter=0
    while (true):
        
        for i in range (nodesxdirection):
            for j in range (nodesydirection):
                Vk0[i][j]=Vk2[i][j]
        
        #Vk0 is the old value 
        #Vk1 is the value after gauss 
        #Vk2 is the value after the Relaxation
        
        #the relaxation takes the old(VK0) and the Gauss output(Vk1) as inputs
        
        
        
        Vk2=Jacobisolve(Vk1,Vk2,deltax,deltay,alpha,beta, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection)
        
        
        i=i+1
        counter=counter+1
        maxres=Residualnew(Vk2,alpha,beta,deltax,deltay, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection,R)
        
        if ( maxres<=Tolerance):
            
            x=Vk2[outputpoint[0]][outputpoint[1]]
            #x=counter
            #x=Vk2
            return  {'x':x, 'Vk2':Vk2 ,'counter':counter }
        else:
            for i in range(i):
                for j in range(j):
                    Vk1[i][j]=Vk2[i][j]
          
           
