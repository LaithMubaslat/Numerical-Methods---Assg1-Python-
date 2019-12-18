#extract matrices from input files ckt1 to ckt5 / Solution
#File:"q1dextractcircuitmatricesfrominputfileandfindsolutions.py"
###############################################################################
###############################################################################

z=ReadMatrices('ckt1')

A=z['A'] #A[0][j]
Ek=z['EK']
Rk=z['RK']
Jk=z['JK']
n=z['n']
k=z['k']
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
for i in range (k):
        Y[i][i]=Rk[i][0]
AT=Transpose(n-1,k,A)
lefthandside=Multiplication(A,Y)
lefthandside=Multiplication(lefthandside,AT)
righthandside= Multiplication(Y,Ek)
for i in range (k): 
    righthandside[i][0]=Jk[i][0]-righthandside[i][0]
b=Multiplication(A,righthandside)
righthandside=b





L=CholskeyL(lefthandside)
y=Lyb(L,righthandside)
X=LTxY (L,y)

###############################################################################
###############################################################################
z=ReadMatrices('ckt2')

A=z['A'] #A[0][j]
Ek=z['EK']
Rk=z['RK']
Jk=z['JK']
n=z['n']
k=z['k']
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
for i in range (k):
        Y[i][i]=Rk[i][0]
AT=Transpose(n-1,k,A)
lefthandside=Multiplication(A,Y)
lefthandside=Multiplication(lefthandside,AT)
righthandside= Multiplication(Y,Ek)

for i in range (k): 
    righthandside[i][0]=Jk[i][0]-righthandside[i][0]
b=Multiplication(A,righthandside)
righthandside=b





L=CholskeyL(lefthandside)
y=Lyb(L,righthandside)
X=LTxY (L,y)


###############################################################################
###############################################################################
z=ReadMatrices('ckt3')

A=z['A'] #A[0][j]
Ek=z['EK']
Rk=z['RK']
Jk=z['JK']
n=z['n']
k=z['k']
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
for i in range (k):
        Y[i][i]=Rk[i][0]
AT=Transpose(n-1,k,A)
lefthandside=Multiplication(A,Y)
lefthandside=Multiplication(lefthandside,AT)
righthandside= Multiplication(Y,Ek)
for i in range (k): 
    righthandside[i][0]=Jk[i][0]-righthandside[i][0]
b=Multiplication(A,righthandside)
righthandside=b





L=CholskeyL(lefthandside)
y=Lyb(L,righthandside)
X=LTxY (L,y)

###############################################################################
###############################################################################
z=ReadMatrices('ckt4')

A=z['A'] #A[0][j]
Ek=z['EK']
Rk=z['RK']
Jk=z['JK']
n=z['n']
k=z['k']
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
for i in range (k):
        Y[i][i]=Rk[i][0]
AT=Transpose(n-1,k,A)
lefthandside=Multiplication(A,Y)
lefthandside=Multiplication(lefthandside,AT)
righthandside= Multiplication(Y,Ek)
for i in range (k): 
    righthandside[i][0]=Jk[i][0]-righthandside[i][0]
b=Multiplication(A,righthandside)
righthandside=b





L=CholskeyL(lefthandside)
y=Lyb(L,righthandside)
X=LTxY (L,y)
###############################################################################
###############################################################################
z=ReadMatrices('ckt5')

A=z['A'] #A[0][j]
Ek=z['EK']
Rk=z['RK']
Jk=z['JK']
n=z['n']
k=z['k']
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
for i in range (k):
        Y[i][i]=Rk[i][0]       
AT=Transpose(n-1,k,A)
lefthandside=Multiplication(A,Y)
lefthandside=Multiplication(lefthandside,AT)
righthandside= Multiplication(Y,Ek)
for i in range (k): 
    righthandside[i][0]=Jk[i][0]-righthandside[i][0]
b=Multiplication(A,righthandside)
righthandside=b





L=CholskeyL(lefthandside)
y=Lyb(L,righthandside)
X=LTxY (L,y)