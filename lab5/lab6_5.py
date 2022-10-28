# Complete the function sum_m_to_n below
def sum_m_to_n(input_m, input_n):
    m = int(input_m)
    n = int(input_n)
    sumx = range(m,n+1)
    sumy = 0
    for sum in sumx:
        sumy = sumy+sum
    return sumy
 
# Output Generation. You are not allowed to modify the following codes
def main():
    input_m = int(input("Enter an integer m please:"))
    input_n = int(input("Enter an integer n please:"))
    return_sum = sum_m_to_n(input_m, input_n)
    print("Sum of all integers in between", input_m, "and", input_n, "is", return_sum)
if __name__ == "__main__":
    main()
