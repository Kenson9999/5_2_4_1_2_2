def is_prime_number(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                break
        else:
            return True
        
def main():
    n = int(input("Input the value n: "))
    total = 0
    output_string = ""
    print("The prime numbers are:")
    for i in range(1,n+1):

        if is_prime_number(i):
            output_string += str(i)+", "
            total+=i
    print (output_string.rsplit(',', 1)[0])
    print("Sum of all prime numbers within 1 and",n,"=",total) 
    
if __name__ == "__main__":
    main()
