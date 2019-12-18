#main 
#map essential code (1)newgauss.py (2)q3final.py 
h=0.0004
w=1.4
#main equal spacing 


Tolerance = 1/100000
deltax=0
deltay=0
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
equalspacing=1

pointx=0.06
pointy=0.04
point=[pointx,pointy] 
alpha=[1]
beta=[1]




deltaxy=[deltax,deltay]
xydimension=[xdimension,ydimension]
Vinnerouter=[Vinner,Vouter]
centercond=[height,width]





Solution=SOR(point,Tolerance,w,deltax,deltay, equalspacing, xydimension,Vinnerouter,centercond,alpha,beta )
Solution         



