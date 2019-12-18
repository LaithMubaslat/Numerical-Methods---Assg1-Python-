#Q1 B
#Building Real, Symmetric, Posetive Definite  Matrices A2,A3,,,,A10
#File:"q1bmatrixbuild.py"

n=2
L2vector=[0]*(n*n)
L2=Matrix(L2vector,n,n)
for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L2[i][j]=(i+1)+(j+1)
L2T=Transpose(n,n,L2)
A2=Multiplication(L2,L2T)

###############################################################################
###############################################################################
n=3
L3vector=[0]*(n*n)
L3=Matrix(L3vector,n,n)

for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L3[i][j]=(i+1)+(j+1)
L3T=Transpose(n,n,L3)
A3=Multiplication(L3,L3T)
###############################################################################
###############################################################################
n=4
L4vector=[0]*(n*n)
L4=Matrix(L4vector,n,n)

for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L4[i][j]=(i+1)+(j+1)
L4T=Transpose(n,n,L4)
A4=Multiplication(L4,L4T)
###############################################################################
###############################################################################
n=5
L5vector=[0]*(n*n)
L5=Matrix(L5vector,n,n)
for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L5[i][j]=(i+1)+(j+1)
L5T=Transpose(n,n,L5)
A5=Multiplication(L5,L5T)
###############################################################################
###############################################################################
n=6
L6vector=[0]*(n*n)
L6=Matrix(L6vector,n,n)

for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L6[i][j]=(i+1)+(j+1)
L6T=Transpose(n,n,L6)
A6=Multiplication(L6,L6T)
###############################################################################
###############################################################################
n=7
L7vector=[0]*(n*n)
L7=Matrix(L7vector,n,n)

for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L7[i][j]=(i+1)+(j+1)
L7T=Transpose(n,n,L7)
A7=Multiplication(L7,L7T)
###############################################################################
###############################################################################
n=8
L8vector=[0]*(n*n)
L8=Matrix(L8vector,n,n)
for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L8[i][j]=(i+1)+(j+1)
L8T=Transpose(n,n,L8)
A8=Multiplication(L8,L8T)
###############################################################################
###############################################################################
n=9
L9vector=[0]*(n*n)
L9=Matrix(L9vector,n,n)
for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L9[i][j]=(i+1)+(j+1)
L9T=Transpose(n,n,L9)
A9=Multiplication(L9,L9T)
###############################################################################
###############################################################################
n=10
L10vector=[0]*(n*n)
L10=Matrix(L10vector,n,n)
for i in range (n) :
    for j in range (n): 
        if i>=j: 
            L10[i][j]=(i+1)+(j+1)
L10T=Transpose(n,n,L10)
A10=Multiplication(L10,L10T)
###############################################################################
###############################################################################