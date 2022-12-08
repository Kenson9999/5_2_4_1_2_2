import sys

COFFEE_NAME_AND_PRICES = (("Cappuccino",25),("Espresso  ",20),("Latte     ",15),("Mocha     ",30))
# Index represented in tuple COFFEE_NAME_AND_PRICES
INDEX_COFFEE_NAME = 0
INDEX_COFFEE_PRICE = 1

# Price of extra option
LARGE_CUP_PRICE = 5
COLD_PRICE = 3

# Index represented in sales tuple. The current_sales_list should contains sales tuples of all unconfirmed order items
INDEX_COFFEE_NO = 0
INDEX_QUANTITY = 1
INDEX_LARGE_CUP = 2
INDEX_COLD = 3

# (i) Complete this function
def display_coffee_shop_menu():
    print("")
    print("Coffee Shop Menu:")
    print("No. | Coffee Type | Price")
    for i in range(len(COFFEE_NAME_AND_PRICES)):
        print(i,"  |",COFFEE_NAME_AND_PRICES[i][INDEX_COFFEE_NAME]," | $"+str(COFFEE_NAME_AND_PRICES[i][INDEX_COFFEE_PRICE]))
    input_coffee_number=input('Please input your choice. Press "Enter" to confirm order (0 – 3):')
    return input_coffee_number

# (ii) Complete this function
def compute_sales(coffee_no, quantity, large_cup, cold):
    coffee_price = COFFEE_NAME_AND_PRICES[coffee_no][INDEX_COFFEE_PRICE]*quantity
    if (large_cup=="Y")|(large_cup=="y"):
        coffee_price+=5*quantity
    if (cold=="Y")|(cold=="y"):
        coffee_price+=3*quantity
    #print(coffee_price)
    return coffee_price

def main():
    current_sales_list = list()
    cups_of_coffee_sold = dict()
    total_number_sales = 0
    highest_sales_amount = 0
    lowest_sales_amount = sys.maxsize
    total_sales_amount = 0
    print("Welcome to Coffee Shop System.")
    while True:
        input_coffee = display_coffee_shop_menu()
        #confirm order
        if (input_coffee == ""):
            if len(current_sales_list) == 0:
                print("Current Sales Order is empty")
                continue
            else:
                # (iv) Complete this part
                total = 0
                #print(current_sales_list)
                for i in current_sales_list:
                    price = compute_sales(i[INDEX_COFFEE_NO], i[INDEX_QUANTITY], i[INDEX_LARGE_CUP], i[INDEX_COLD])
                    total += price

                # compute total sales
                total_number_sales+=1
                total_sales_amount+=total
                if total > highest_sales_amount:
                    highest_sales_amount = total
                if total < lowest_sales_amount:
                    lowest_sales_amount = total
                print("\nStatistics of Coffee Shop:")
                print ("Total number sales = "+str(total_number_sales))
                print ("Lowest Sales Amount = $"+str(lowest_sales_amount))
                print ("Highest Sales Amount = $"+str(highest_sales_amount))
                print ("Total Sales Amount = $"+str(total_sales_amount))
                print ("Average Sales Amount = $"+str(total_sales_amount / total_number_sales))

                print("List of number of cups coffee sold:")
                for i in current_sales_list:
                    sold_coffee_name=COFFEE_NAME_AND_PRICES[i[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME].rstrip()
                    sold_coffee_quantity=i[INDEX_QUANTITY]
                    #print(sold_coffee_name,sold_coffee_quantity)
                    if sold_coffee_name not in cups_of_coffee_sold:
                        cups_of_coffee_sold[sold_coffee_name]=sold_coffee_quantity
                    else:
                        cups_of_coffee_sold[sold_coffee_name]=cups_of_coffee_sold[sold_coffee_name]+sold_coffee_quantity
                current_sales_list.clear()
                for number, name in sorted(cups_of_coffee_sold.items(), reverse=False):
                    print("	",number,":" ,name)

        else:
            # for user to input coffee type, quantity, large or not, cold or not
            input_coffee = int(input_coffee)
            input_quantity = int(input("Please input quantity:"))
            input_large_cup = input("Large Cup required? +$5.00 (Y / N):").upper()
            input_cold = input("Cold required? +$3.00 (Y / N):").upper()
            
            current_sales_record = (input_coffee, input_quantity, input_large_cup, input_cold)
            current_sales_list.append(current_sales_record)
            
            print("\nCurrent Order Summary:")
            #print(current_sales_list)
            total = 0
            for i in current_sales_list:
                #print(i)
                this_coffee_option = ""
                current_sales_COFFEE_NAME=COFFEE_NAME_AND_PRICES[i[INDEX_COFFEE_NO]][INDEX_COFFEE_NAME]
                current_sales_COFFEE_PRICES=COFFEE_NAME_AND_PRICES[i[INDEX_COFFEE_NO]][INDEX_COFFEE_PRICE]*i[INDEX_QUANTITY]
                current_sales_LARGE_CUP=i[INDEX_LARGE_CUP]
                current_sales_COLD=i[INDEX_COLD]
                this_coffee_cost=current_sales_COFFEE_PRICES
                if (current_sales_LARGE_CUP =="Y")|(current_sales_LARGE_CUP =="y")|(current_sales_COLD =="Y")|(current_sales_COLD =="y"):
                    this_coffee_option =" with option "
                    if ((current_sales_COLD =="N")|(current_sales_COLD =="n"))&((current_sales_LARGE_CUP =="Y")|(current_sales_LARGE_CUP =="y")):
                        this_coffee_option+="LARGE CUP"
                        this_coffee_cost+=5*i[INDEX_QUANTITY]
                    if ((current_sales_COLD =="Y")|(current_sales_COLD =="y"))&((current_sales_LARGE_CUP =="N")|(current_sales_LARGE_CUP =="n")):
                        this_coffee_option+="COLD"
                        this_coffee_cost+=3*i[INDEX_QUANTITY]
                    if ((current_sales_COLD =="Y")|(current_sales_COLD =="y"))&((current_sales_LARGE_CUP =="Y")|(current_sales_LARGE_CUP =="y")):
                        this_coffee_option+="COLD LARGE CUP"
                        this_coffee_cost+=8*i[INDEX_QUANTITY]
                        
                total+=this_coffee_cost

                print(current_sales_COFFEE_NAME.rstrip(),i[INDEX_QUANTITY],"cups"+str(this_coffee_option)+": $"+str(this_coffee_cost))
            current_sales_total_string = "Total: $"
            print(current_sales_total_string+str(total))

            # i is tuple in the format (0, 3, 'Y', 'Y')
            # compute_sales for each coffee

            # (iii) Complete this part
            
if __name__ == "__main__":
    main()
