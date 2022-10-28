# Complete the function greeting below
def greeting(*name):
    for n in name:
        print("Hello!"+n)
    
 
# Output Generation. You are not allowed to modify the following codes
def main():
    greeting ("Alice")
    greeting ("Sam", "Susan")
    greeting ("Kelvin", "Peter", "Mary")
if __name__ == "__main__":
    main()
