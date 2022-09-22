money = input ("Money?")

ten = int(money)/10
five = (int(money)%10)/5
two = ((int(money)%10)%5)/2
one = (((int(money)%10)%5)%2)/1
print(int(ten),"10-dollar coin(s)")
print(int(five),"5-dollar coin(s)")
print(int(two),"2-dollar coin(s)")
print(int(one),"1-dollar coin(s)")
