print ("Module a is loaded")
print (__name__)
 
def print_a():
    print("Print function in file a.py is executed")
 
if __name__ == "__main__":
    print_a()
