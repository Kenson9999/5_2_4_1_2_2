list = []
for i in range(1,4):
    for n in range(1,6):
        list.append((str(i)+"-"+str(n)))
    print("\t".join(list))
    list = []