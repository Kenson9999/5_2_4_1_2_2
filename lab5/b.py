print ("Module b is loaded")
print (__name__)
print (type(__name__))
import a
 
def print_b():
    print("Print function in file b.py is executed")
 
if __name__ == "__main__":
    print_b()
