list = []
n = int(input("Input table size n:"))
x = range(1,n+1)
for i in x:
    list.append(str(i))
print("\t","\t ".join(list))
print("")
for i in x:
    print(i,"\t",i,"\t",i*2,"\t",i*3,"\t",i*4)
    
    
    