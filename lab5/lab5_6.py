lower_limit = int(input("Input lower limit:"))
upper_limit = int(input("Input upper limit:"))
n = int(input("Input divisor (n):"))
sumx=0
if lower_limit>upper_limit:
    new_lower_limit = lower_limit
    lower_limit = upper_limit
    upper_limit = new_lower_limit
elif lower_limit==upper_limit:
    print("==?")
else:
    pass
x = range(lower_limit,upper_limit+1)
for y in x:
    if (y%n)==0:
        sumx+=y
        print("i =",y,"sum =",sumx)
print("Sum of all numbers divisible by n:",sumx)