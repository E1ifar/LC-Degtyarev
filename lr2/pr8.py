import math
x=-2.235*10**-2;
y=2.23;
z=15.221;
s=(math.e**math.fabs(x-y)*math.fabs(x-y)**(x+y))/(math.atan(x)+math.atan(z))+(x**6+math.log(y,math.e)**2)**(1/3);
print(s);