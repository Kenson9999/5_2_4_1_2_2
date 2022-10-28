# Complete the function quadratic below
def quadratic(a=0,b=0,c=0):
    if a==0:
        return "This is not a quadratic equation"
    else:
        discriminant = (b * b - 4 * a * c)
        if discriminant > 0:   # two roots
            x1= (-b + discriminant ** 0.5) / (2 * a)
            x2= (-b - discriminant ** 0.5) / (2 * a)
            return f"2 roots, x1 ={x1}, x2 = {x2}"
        elif discriminant == 0: # one root:
            x= -b / (2 * a)
            return f"1 root, x ={x}"
        else: # no roots
            return "No real roots"
    
# Output Generation. You are not allowed to modify the following codes
def main():
    print (type(quadratic(b=1,c=-1)))
    print (quadratic(a=1,c=-1))
    print (quadratic(a=1,b=-1))
    print (quadratic(1,-2,1))
    print (quadratic(1,1,1))
    print (quadratic(3,-4,1))
if __name__ == "__main__":
    main()
