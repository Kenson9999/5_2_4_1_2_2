# Complete the function sum_to_n below
def sum_to_n(input_n):
    n = int(input_n)
    sumx = range(n+1)
    sumy = 0
    for sum in sumx:
        sumy = sumy+sum
    return sumy
# Output Generation. You are not allowed to modify the following codes
def main():
    input_n = int(input("Enter an integer n please:"))
    return_sum = sum_to_n(input_n)
    print("Sum of all integers in between 1 to", input_n, "is", return_sum)
if __name__ == "__main__":
    main()
