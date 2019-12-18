#new gauss 

#q3 test 





def Gauss(Vk1,deltax,deltay,alpha,beta, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection):
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
            Vk1[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk1[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk1[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk1[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk1[i][j]= term1 *             Vk1[i][j]
        
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
            Vk1[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk1[i][j]=  (term2 * alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk1[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk1[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk1[i][j]= term1 *             Vk1[i][j]
        
            
        
            
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
        Vk1[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
        Vk1[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
        Vk1[i][j]= (term3 * beta1 * Vk1[i][j-1]) +               Vk1[i][j]
        Vk1[i][j]= (term3*beta1 * Vk1[i][j-1]) +                Vk1[i][j]
        Vk1[i][j]= term1 *             Vk1[i][j]
        
            
        
        
        
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
            Vk1[i][j]= (term2 * alpha2 * Vk1[i-1][j]) 
            Vk1[i][j]=  (term2 *  alpha1 * Vk1[i+1][j] )          + Vk1[i][j]
            Vk1[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
            Vk1[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
            Vk1[i][j]= term1 *             Vk1[i][j]
        
            
                
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
        Vk1[i][j]= (term2 * alpha1 * Vk1[i-1][j]) 
        Vk1[i][j]=  (term2 * alpha1 * Vk1[i-1][j] )          + Vk1[i][j]
        Vk1[i][j]= (term3 * beta2 * Vk1[i][j-1]) +               Vk1[i][j]
        Vk1[i][j]= (term3*beta1 * Vk1[i][j+1]) +                Vk1[i][j]
        Vk1[i][j]= term1 *             Vk1[i][j]
        
            
    return Vk1

def Residual(Vk2,bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection,R):
    
    max=0
    
    for i in range (1,nodesxdirection-1):
        for j in range (1,nodesydirection-1):
            z= Vk2[i+1][j]
            z= Vk2[i-1][j] + z
            z= Vk2[i][j+1]+ z
            z= Vk2[i][j-1]+ z
            z= z - 4 * Vk2[i][j] 
            R[i][j]=z
            # to be modified 
    # I get the effect of the internal conductor then I zero it's terms in the matrix
 
            
            #boundary nodes /making use of symmetry 
            
            
    j=nodesydirection-1
    for i in range (1,bottomleftedgeXnode):
        z=Vk2[i-1][j]
        z=z+Vk2[i+1][j]
        z=z+Vk2[i][j-1]
        z=z+Vk2[i][j-1]
        z=z-4 * Vk2[i][j] 
                
        R[i][j]=z
    i=nodesxdirection-1  
    for j in range (1,bottomleftedgeYnode):
        z=Vk2[i-1][j]
        z= Vk2[i-1][j] + z
        z=Vk2[i][j-1]+ z
        z=Vk2[i][j+1]+ z
        z=z-4 * Vk2[i][j] 
        R[i][j]=z
            
                
            
    for i in range (bottomleftedgeXnode,nodesxdirection):
        for j in range (bottomleftedgeYnode,nodesydirection):
            R[i][j]=0
            
    i=0
    for j in range (nodesydirection):
        R[i][j]=0
    
    j=0
    for i in range (nodesxdirection):
        R[i][j]=0 
    
    
            
    for i in range (nodesxdirection):
        for j in range (nodesydirection):
            if R[i][j]>max:
                max=R[i][j]
  
                    
                
            
    return max
     
def SORaddition(Vk0,Vk1,w,nodesxdirection,nodesydirection):
    for i in range (nodesxdirection):
        for j in range (nodesydirection):
            Vk1[i][j]=(1-w)*Vk0[i][j]+(w)*Vk1[i][j] 
    
    return Vk1


def Residualnew(Vk2,alpha,beta,deltax,deltay, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection,R):
    
    max=0 
    
    #designed s.t. deltax=delta y for consistency of results
    
    for i in range (1,nodesxdirection-1):
        for j in range (1,nodesydirection-1):
            alpha1=alpha[i-1]
            alpha2=alpha[i]
            beta1=beta[j-1]
            beta2=beta[j]
            
            x=Vk2[i][j]
            
            z1= (Vk2[i+1][j]-x)/(alpha2*(alpha1+alpha2))
            z1= (Vk2[i-1][j]-x)/(alpha1*(alpha1+alpha2)) + z1
            z1=z1*2
            z2= (Vk2[i][j+1]-x)/(beta2*(beta1+beta2))
            z2= (Vk2[i][j-1]-x)/(beta1*(beta1+beta2))+ z2
            z2=  z2*2
            R[i][j]=z1+z2
           
    # I get the effect of the internal conductor then I zero it's terms in the matrix
 
          
            #boundary nodes /making use of symmetry 
            
            
    j=nodesydirection-1
    for i in range (1,bottomleftedgeXnode):
        
        alpha1=alpha[i-1]
        alpha2=alpha[i]
        beta1=beta[j-1]
        beta2=beta1
            
        
        x=Vk2[i][j]
        
        z1=(Vk2[i-1][j]-x)/(alpha1*(alpha1+alpha2))
        z1=(Vk2[i+1][j]-x)/(alpha2*(alpha1+alpha2)) +z1
        
        z1=z1*2
        
        z2=(Vk2[i][j-1]-x)/(beta1*(beta1+beta2))
        z2=(Vk2[i][j-1]-x)/(beta1*(beta1+beta2))+z2
        
        z2=  z2*2
        
        
        z=z1+z2
                
        R[i][j]=z
        
        
        
        
        
    i=nodesxdirection-1  
    for j in range (1,bottomleftedgeYnode):
        
        
        alpha1=alpha[i-1]
        alpha2=alpha1
        beta1=beta[j-1]
        beta2=beta[j]
            
        x=Vk2[i][j]
        
        z1=(Vk2[i-1][j]-x)/(alpha1*(alpha1+alpha2))
        z1= (Vk2[i-1][j]-x)/(alpha1*(alpha1+alpha2)) + z1
        
        
        z1=z1*2
        
        z2=(Vk2[i][j-1]-x) /(beta1*(beta1+beta2))
        z2=(Vk2[i][j+1]-x)/(beta2*(beta1+beta2)) + z2
        
        z2=  z2*2
        
        z=z1+z2
        
        
        R[i][j]=z
        
        
            
        #la hooooooon     
            
    for i in range (bottomleftedgeXnode,nodesxdirection):
        for j in range (bottomleftedgeYnode,nodesydirection):
            R[i][j]=0
            
    i=0
    for j in range (nodesydirection):
        R[i][j]=0
    
    j=0
    for i in range (nodesxdirection):
        R[i][j]=0 
    
    
            
    for i in range (nodesxdirection):
        for j in range (nodesydirection):
            if R[i][j]>max:
                max=R[i][j]
  
                    
                
            
    return max
