from calendar import month


y=int(input("Enter Year: "))
m=int(input("Enter Month: "))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("Number of days in this month: 31")
elif m==4 or m==6 or m==9 or m==11:
    print("Number of days in this month: 30")
elif 