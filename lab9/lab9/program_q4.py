def quadratic(a=0, b=0, c=0):
    output = ""
    if a==0:
        output = "This is not a quadratic equation"
        return output
    else:
        discriminant = (b * b - 4 * a * c)
        if discriminant > 0:   # two roots
            x1= (-b + discriminant ** 0.5) / (2 * a)
            x2= (-b - discriminant ** 0.5) / (2 * a)
            output = "2 roots, x1 = "+str(x1)+", x2 = "+str(x2)
            return output
        elif discriminant == 0: # one root:
            x= -b / (2 * a)
            output = "1 root, x ="+str(x)
            return output
            
        else: # no roots
            output = "No real roots"
            return output
            

def main():
    print (quadratic(3,-4, 1))
    print (quadratic(1,-2))

if __name__ == "__main__":
    main()
