# Complete the function factorial below
def factorial(input_n):
    return 1 if (input_n==1 or input_n==0) else input_n * factorial(input_n - 1);
    #https://www.javatpoint.com/pyhton-factorial-number
# Output Generation. You are not allowed to modify the following codes
def main():
    input_n = int(input("Enter an integer n please:"))
    return_value = factorial(input_n)
    print(str(input_n) + "! =", return_value)
if __name__ == "__main__":
 main()
