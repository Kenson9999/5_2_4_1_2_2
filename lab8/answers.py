#q1
input_length = int( input("Input length in centimeter(cm): ") )

if input_length < 100:	
    output_cm = input_length	
    output_string = str ( output_cm ) + "cm"	

elif input_length < 1000 * 100:	
    output_m = int ( input_length / 100 )	
    output_cm = input_length % 100	
    output_string = str (output_m ) + "m and " + str ( output_cm ) + "cm"	

else:
    output_km = int ( input_length / 1000 /100 )	
    output_m = int ( input_length % (1000*100) / 100 )	
    output_cm = input_length % 1000 % 100	
    output_string = str (output_km ) + "km, " + str ( output_m ) + "m and " + str ( output_cm ) + "cm"	

print ("There are " + output_string )


#q2
n = int ( input ( "Input the size:" ) )	
for row in range ( n , 0 , -1 ):	
        output = ""	
        for column in range ( 1 , row + 1 ):	
                output += str (column) + " "	
        print(output)

#q3
sum=0

i=0
while i < 13:
    sum = sum + i
    i = i + 5

print (sum)

#q4
def average_marks ( list_marks ) :
    total = 0
    for mark in list_marks:
        total += int (mark)
    return total / len ( list_marks )

#q5
def display_students(students):
    for i in students:
        student = i.split(" ")
        print ("Student ID:",student[0])
        print ("Student Name:", student[1])
        print ("Average Marks:", average_marks(student[2:]))
        print ("---")
    
    print ("Total students:", len(students))


# You are not allowed to modify the following codes
def main():
    students = [
        "221234567 kelvinyip 95 75 45 68 82 86 52",
        "220924358 cowleung 23 45 0 57 12 38 53",
        "220123854 peterpan 35 54 76 52 68 49 57"
    ]
    display_students(students)

if __name__ == "__main__":
    main()

#q6a
def display_menu ( ):	
    print ("Select Transaction Type:")	
    print ("1. Deposit")	
    print ("2. Withdraw")	
    return input()

#q6b
# initialize the variable balance
balance = 0

# use looping so that the program would call the display_menu() function 
# continuously for display and user input
while True:
    # call the display_menu() function and assign the returned value of this 
    # function to variable transaction_type
    transaction_type = display_menu()

    # put your statements here if user inputted 1 for deposit in the select 
    # transaction type menu
    if transaction_type == "1":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount


        pass
    # put your statements here if user inputted 2 for withdraw in the select 
    # transaction type menu
    elif transaction_type == "2":
        amount = int(input("Enter withdraw amount: "))
        if (amount > balance):
            balance = balance - 10
            print("Insufficient Balance, $10.00 Service Charge")
        else:
            balance = balance - amount


        pass
    #put all other necessary logics here 
    else:
        continue

    #print the balance here
    print ("Balance :", balance)


#q1 1x marks
#          6 
#        5 5 
#      4 4 4 
#    3 3 3 3 
#  2 2 2 2 2 
#1 1 1 1 1 1 

#q2 function definition and usage 20 marks

#q3 try except valueerror 10 marks

#q4a display list of dictionary assingment 7 marks

#q4b prepare list of dictionary read from file 14 marks

#q5 troubleshotting 1x marks
