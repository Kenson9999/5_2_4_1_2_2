n = int(input("Input the value n:"))
x = range(2,n+1,+2)
sumx = 0
list = []
for y in x:
    sumx=sumx+y
    list.append(str(y))
    #print(y)
print(",".join(list))
print("Sum of all even numbers within 1 and "+str(n)+" = "+str(sumx))