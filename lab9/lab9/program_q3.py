import random

def display(list_numbers):
    print ("Sum =", sum(list_numbers))
    print ("Average =", sum(list_numbers)/len(list_numbers))
    print ("Minimum =", min(list_numbers))
    print ("Maximum =", max(list_numbers))
    
def create_random_number(no_of_random_numbers):
    list_random_numbers = list()
    for i in range(no_of_random_numbers):
        list_random_numbers.append( random.randint(1, 100) )
        print (f"Number {i} is {list_random_numbers[i]}")
    return list_random_numbers
    
def main():
    no_of_random_numbers = int(input("Number of random numbers: "))
    list_random_number = create_random_number(no_of_random_numbers)
    display(list_random_number)

if __name__ == "__main__":
    main()
