#Test 2 Getting x from A b (output is Xnhat: Input An and bn matrices)
#File:"q1cproducexhat.py"

#Lhat was obtained in an earlier segment of the code and so is being used here to compute Xhat 
###############################################################################
###############################################################################
n=2
L=L2hat
b=b2
y=Lyb(L,b)
X2hat=LTxY (L,y)
X2error=0
for i in range (n): 
    X2error=X2error+ (x2[i]-X2hat[i][0])*(x2[i]-X2hat[i][0])
###############################################################################
###############################################################################
n=3
L=L3hat
b=b3
y=Lyb(L,b)
X3hat=LTxY (L,y)
X3error=0
for i in range (n): 
    X3error=X3error+ (x3[i]-X3hat[i][0])*(x3[i]-X3hat[i][0])
###############################################################################
###############################################################################
n=4
L=L4hat
b=b4
y=Lyb(L,b)
X4hat=LTxY (L,y)
X4error=0
for i in range (n): 
    X4error=X4error+ (x4[i]-X4hat[i][0])*(x4[i]-X4hat[i][0])
###############################################################################
###############################################################################
n=5
L=L5hat
b=b5
y=Lyb(L,b)
X5hat=LTxY (L,y)
X5error=0
for i in range (n): 
    X5error=X5error+ (x5[i]-X5hat[i][0])*(x5[i]-X5hat[i][0])
###############################################################################
###############################################################################
n=6
L=L6hat
b=b6
y=Lyb(L,b)
X6hat=LTxY (L,y)
X6error=0
for i in range (n): 
    X6error=X6error+ (x6[i]-X6hat[i][0])*(x6[i]-X6hat[i][0])
###############################################################################
###############################################################################
n=7
L=L7hat
b=b7
y=Lyb(L,b)
X7hat=LTxY (L,y)
X7error=0
for i in range (n): 
    X7error=X7error+ (x7[i]-X7hat[i][0])*(x7[i]-X7hat[i][0])
###############################################################################
###############################################################################
n=8
L=L8hat
b=b8
y=Lyb(L,b)
X8hat=LTxY (L,y)
X8error=0
for i in range (n): 
    X8error=X8error+ (x8[i]-X8hat[i][0])*(x8[i]-X8hat[i][0])
###############################################################################
###############################################################################
n=9
L=L9hat
b=b9
y=Lyb(L,b)
X9hat=LTxY (L,y)
X9error=0
for i in range (n): 
    X9error=X9error+ (x9[i]-X9hat[i][0])*(x9[i]-X9hat[i][0])
###############################################################################
###############################################################################
n=10
L=L10hat
b=b10
y=Lyb(L,b)
X10hat=LTxY (L,y)
X10error=0
for i in range (n): 
    X10error=X10error+ (x10[i]-X10hat[i][0])*(x10[i]-X10hat[i][0])
###############################################################################
###############################################################################
