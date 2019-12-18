#creating the input files for the circuits
###############################################################################
###############################################################################
#circuit 1 
n=2
k=2
A=[-1, -1]
Rk=[1/10, 1/10]
Ek=[10,0]
Jk=[0,0]
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
A=Matrix(A,n-1,k)
for i in range (k):
        Y[i][i]=Rk[i]
Ek=Matrix(Ek,k,1)
Jk=Matrix(Jk,k,1)
Rk=Matrix(Rk,k,1)
Networkname='ckt1'
SaveNetworkMatricesAsText(Networkname,Jk,Rk,Ek,A,n,k)
###############################################################################
###############################################################################
#circuit 2 
n=2
k=2
A=[1, 1]
Rk=[0.1, 0.1]
Ek=[0,0]
Jk=[10,0]
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
A=Matrix(A,n-1,k)
for i in range (k):
        Y[i][i]=Rk[i]
Ek=Matrix(Ek,k,1)
Jk=Matrix(Jk,k,1)
Rk=Matrix(Rk,k,1)
Networkname='ckt2'
SaveNetworkMatricesAsText(Networkname,Jk,Rk,Ek,A,n,k)
###############################################################################
###############################################################################
#circuit 3 
n=2
k=2
A=[-1, 1]
Rk=[1/10, 1/10]
Ek=[10,0]
Jk=[0,10]
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
A=Matrix(A,n-1,k)
for i in range (k):
        Y[i][i]=Rk[i]
Ek=Matrix(Ek,k,1)
Jk=Matrix(Jk,k,1)
Rk=Matrix(Rk,k,1)
Networkname='ckt3'
SaveNetworkMatricesAsText(Networkname,Jk,Rk,Ek,A,n,k)
###############################################################################
###############################################################################
#circuit 4
n=3
k=4
A=[-1, 1,1,0,0,0,-1,1]
Rk=[1/10, 1/10,1/5,1/5]
Ek=[10,0,0,0]
Jk=[0,0,0,10]
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
A=Matrix(A,n-1,k)
for i in range (k):
        Y[i][i]=Rk[i]
Ek=Matrix(Ek,k,1)
Jk=Matrix(Jk,k,1)
Rk=Matrix(Rk,k,1)
Networkname='ckt4'
SaveNetworkMatricesAsText(Networkname,Jk,Rk,Ek,A,n,k)
###############################################################################
###############################################################################
#circuit 5 
n=4
k=6
A=[-1, 1,1,0,0,0,0,-1,0,1,1,0,0,0,-1,-1,0,1]
Rk=[1/20, 1/10,1/10,1/30,1/30,1/30]
Ek=[10,0,0,0,0,0]
Jk=[0,0,0,0,0,0]
Y=[0]*(k*k)
Y=Matrix(Y,k,k)
A=Matrix(A,n-1,k)
for i in range (k):
        Y[i][i]=Rk[i]
Ek=Matrix(Ek,k,1)
Jk=Matrix(Jk,k,1)
Rk=Matrix(Rk,k,1)
Networkname='ckt5'
SaveNetworkMatricesAsText(Networkname,Jk,Rk,Ek,A,n,k)
###############################################################################
###############################################################################