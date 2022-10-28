# Complete the function cube_of_n below
def cube_of_n(n):
    cube_n = n*n*n
    return cube_n
# Complete the function show_instruction below
def show_instruction():
    print("This program computes cube of n")

# Complete the function get_n below
def get_n():
    n = int(input("Enter an integer N please:"))
    return n
# Output Generation. You are not allowed to modify the following codes
def main():
    show_instruction()
    n = get_n()
    cube_n = cube_of_n(n)
    print("Cube of", n, "=", cube_n)
if __name__ == "__main__":
    main()
