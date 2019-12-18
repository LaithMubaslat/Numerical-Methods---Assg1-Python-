#SOR code 






              
def SOR(point,T,w,deltax,deltay, equalspacing, xydimension,Vinnerouter,centercond,alpha,beta ): 
    
    
    
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
    
    
    
    
    #check validity of alpha/beta values 
    
    if equalspacing!=1: 
        checkx=0
        checky=0
        innerconductoredgextest=0 #inclusion of inner conductor edge x
        innerconductoredgeytest=0 #inclusion of inner conductor edge y
        nodesxdirection = rowdimension(alpha) +1 
        nodesydirection = rowdimension(beta) +1 
        n=nodesxdirection* nodesydirection #total number of nodes
        n=int(n)
        
        
        
        for i in range (nodesxdirection-1): 
            
            
            checkx=checkx+alpha[i]*deltax
            
            #checks if edges of inner conductor are accounted for by alpha,beta,deltax,deltay parameters
            if (round(checkx, 10)==round(edgex, 10)):
                innerconductoredgextest=int(1)
                bottomleftedgeXnode=i+1
                
                
             #checks if edges of desired point x coordinate is located at a node
            if (round(checkx, 10)==round(point[0], 10)):
                pointcoordinateXcheck=int(1)
                outputnodex=i+1
              
                
            
            
    
            
            #to check whether alpha,beta,deltax,deltay cover internal conductor edges which 
            #which are essential for a correct solution for the problem
            
        for i in range (nodesydirection-1): 
            
            

            checky=checky+beta[i]*deltay
            
            #checks if edges of inner conductor are accounted for by alpha,beta,deltax,deltay parameters
       
            
            if (round(checky, 10)==round(edgey, 10)):
                innerconductoredgeytest=int(1)
                bottomleftedgeYnode=i+1
            
            
            #checks if edges of desired point y coordinate is located at a node
            if (round(checky, 10)==round(point[1], 10)):
                pointcoordinateYcheck=int(1)
                outputnodey=j+1
            
            
            
        #to check compatibility of alpha, beta, deltax deltay with problem  geometry
        
        if (round(checkx,10)!= (round(xydimension[0]/2,10))): 
            print("alpha parameters and deltax invalid for problem geometry ")
            return 
        if (round(checky,10)!= round((xydimension [1]/2),10)):
            print("beta parameters and deltay invalid for problem geometry ")
            return 
        
        if (innerconductoredgextest==0):
            print("alpha parameters and deltax invalid for inclusion of inner conductor edges")
            return 
            
        if (innerconductoredgeytest==0): 
            print("beta parameters and deltay invalid for inclusion of inner conductor edges ")
            return 
        
        
    
        
            
    
        

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
        
        
        
        Vk1=Gauss(Vk2,deltax,deltay,alpha,beta, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection)
        Vk2=SORaddition(Vk0,Vk1,w,nodesxdirection,nodesydirection)
        
        i=i+1
        counter=counter+1
        maxres=Residualnew(Vk2,alpha,beta,deltax,deltay, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection,R)
        
        if ( maxres<=Tolerance):
            
            x=Vk2[outputpoint[0]][outputpoint[1]]
            #x=counter
            #x=Vk2
            
            
            
            return  {'x':x, 'Vk2':Vk2 ,'counter':counter }
          
           
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
  ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################
 ############################################################################








