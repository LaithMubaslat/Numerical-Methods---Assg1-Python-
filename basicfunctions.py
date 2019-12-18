##### BasicFunctions
from math import sqrt


def VerticalVector(HorizontalVector,dimension):
    n=dimension
    V=[0]*(n*n)
    for i in range (n*n):
        if ((i%n)==0): V[i]=HorizontalVector[i//n]
        
    VV=Matrix(V,n,1)
    
    return VV
#function to create a matrix 
def Matrix(dataList,rows,columns ):
    Matrix = []
    counter=0
    for i in range(rows):
        rowList = []
        for j in range(columns):
            # you need to increment through dataList here, like this:
            rowList.append(dataList[counter])
            counter=counter+1
        Matrix.append(rowList)

    return Matrix
def SqMatrix(dataList,n):
    Matrix = []
    for i in range(n):
        rows = []
        for j in range(n):
            # you need to increment through dataList here, like this:
            rows.append(dataList[n * i + j])
        Matrix.append(rows)

    return Matrix
def rowdimension(s):
    return 1 + rowdimension(s[1:]) if s else 0
def columndimension(s):
    x=s[0]    
    return  rowdimension(x)
#searches for largest value in square matrix of size n returns index of that value 
def TransposeSquare(rows,columns,M): 
    MTinit=[0]*(n*n)
    MT=Matrix(MTinit,rows,columns)
    for i in range (rows):
        for j in range (columns): 
           
                MT[i][j]=M[j][i]               
    return MT
def Transpose(rows,columns,M): 
    MTinit=[0]*(rows*columns)
    MT=Matrix(MTinit,columns,rows)
    for j in range (columns):
        for i in range (rows): 
           
                MT[j][i]=M[i][j]               
    return MT        
def Multiplication (M1,M2):
    r1=rowdimension(M1)
    c1=columndimension(M1)
    
    r2=rowdimension(M2)
    c2=columndimension(M2)    
    Productzeros=[0]*(r1*c2)
    Product=Matrix(Productzeros,r1,c2)   
    if (c1!=r2):
        print("Matrix Multiplication is Invalid: Column count of first does not equal Row count of Second")
        return        
    for i in range (r1):
        for j in range (c2): 
            for k in range (c1):
                Product[i][j] = Product [i][j]+ M1[i][k]*M2[k][j]
    return Product
def MatrixVectorMultiplication(M1,V): #MV1=V2
    r1=rowdimension(M1)
    c1=columndimension(M1)    
    r2=rowdimension(V)
    c2=1   
    Productzeros=[0]*(c1*r2)
    Product=VerticalVector(Productzeros,r1*c2)    
    if (c1!=r2):
        print("Matrix Multiplication is Invalid: Column count of first does not equal Row count of Second")
        return       
    for i in range (r1):
            for k in range (c1):
                    Product[i][0] = Product [i][0]+ M1[i][k]*V[k]
    return Product
