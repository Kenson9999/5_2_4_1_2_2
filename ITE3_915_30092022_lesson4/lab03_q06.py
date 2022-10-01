import math

a=int(input("Input the value a:"))
b=int(input("Input the value b:"))
c=int(input("Input the value c:"))
d=(int(b)**2)-(4*int(a)*int(c))
if a==0 & d<=0:
    print("This is not a quadratic equation")
elif d>0:
    print("2 roots, x1=",((-(int(b)))+(math.sqrt((int(b)**2)-(4*int(a)*int(c)))))/(2*int(a)),"x2=",((-(int(b)))-(math.sqrt(int(b)**2-(4*int(a)*int(c)))))/(2*int(a)))
elif d==0:
    print("1 roots,x=",((-(int(b)))+(math.sqrt((int(b)**2)-(4*int(a)*int(c)))))/(2*int(a)))
elif d<0:
    print("No real roots")
else:
    print("error")


# x1 = ((-(int(b)))+(math.sqrt((int(b)**2)-(4*int(a)*int(c)))))/(2*int(a))
# x2 = ((-(int(b)))-(math.sqrt(int(b)**2-(4*int(a)*int(c)))))/(2*int(a))
# print("x1=",x1)
# print("x2=",x2)