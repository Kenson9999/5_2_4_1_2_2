import math

a=input("Input the value a:")
b=input("Input the value b:")
c=input("Input the value c:")
x1 = ((-(int(b)))+(math.sqrt((int(b)**2)-(4*int(a)*int(c)))))/(2*int(a))
x2 = ((-(int(b)))-(math.sqrt(int(b)**2-(4*int(a)*int(c)))))/(2*int(a))
print("x1=",x1)
print("x2=",x2)