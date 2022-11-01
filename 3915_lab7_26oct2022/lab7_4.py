# your code goes here
import random
def create_list_random_number(no_of_random_number, min_random_number, max_random_number):
    randam_numbers_list=list()
    for i in range(no_of_random_number):
        random_number = random.randint(min_random_number, max_random_number)
        randam_numbers_list.append(random_number)
    return randam_numbers_list

    
# Output Generation. You are not allowed to modify the following codes
def main():
    no_of_random_number = int(input("How many random numbers?"))
    min_random_number = int(input("Minimum value of random numbers:"))
    max_random_number = int(input("Maximum value of random numbers:"))
    list_random_number = create_list_random_number(no_of_random_number, min_random_number, max_random_number)
    # your code goes here
    print(list_random_number)
    while True:
        change_number_index = int(input("Input an index you’d like to change: "))
        change_number_value = int(input("Input the value you’d like to change:"))
        list_random_number[change_number_index] = change_number_value
        print(list_random_number)
if __name__ == "__main__":
    main()
