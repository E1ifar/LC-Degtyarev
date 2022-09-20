import math
x=2.444;
y=0.869*10**-2;
z=-0.13*10**3;
s=((x**(y+1)+math.e**(y-1))/(1+x*math.fabs(y-math.tan(z))))*(1+math.fabs(y-x))+((math.fabs(y-x)**2)/2)-((math.fabs(y-x)**3)/3);
print(s);