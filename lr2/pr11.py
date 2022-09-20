import math
x=6.251;
y=0.827;
z=25.001;
s=y**((math.fabs(x))**(1/3))+(math.cos(y)**3)*((math.fabs(x-y)*(1+((math.sin(z)**2)/(math.sqrt(x+y))))))/(math.e**(math.fabs(x-y))+x/2);
print(s);