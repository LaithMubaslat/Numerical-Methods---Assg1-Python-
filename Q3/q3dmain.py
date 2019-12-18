#q3dmain


#main unequal 



Tolerance = 1/100000
h=0.02
deltax=0.01
deltay=0.01




#dimensions of the outer conductor
xdimension=0.2
ydimension= 0.2
#conductor voltages
Vinner=110
Vouter=0
#inner conductor height and width
height=0.04
width=0.08
#equalspacing
equalspacing=0


pointx=0.06
pointy=0.04

point=[pointx,pointy] 



alpha=[0.1,0.4,1.6,1.8,1.2,            0.9   ,                 0.9 ,        0.9 ,        1 ,      1.2]  #4
beta=[0.1,1.1,2,1.4,1.4,1.2,0.8 ,                  0.6 ,0.7,0.7]

sum=0
for i in range(10):
    sum=beta[i]+sum

deltaxy=[deltax,deltay]
xydimension=[xdimension,ydimension]
Vinnerouter=[Vinner,Vouter]
centercond=[height,width]





Vk2 = Jacobisolve (deltax,deltay,alpha,beta, bottomleftedgeXnode,bottomleftedgeYnode,nodesxdirection,nodesydirection)

for i in range (nodesxdirection):
        for j in range (nodesydirection):
            Vk1[i][j]=Vk2[i][j]






Solution=SOR(point,Tolerance,w,deltax,deltay, equalspacing, xydimension,Vinnerouter,centercond,alpha,beta )      
Solution