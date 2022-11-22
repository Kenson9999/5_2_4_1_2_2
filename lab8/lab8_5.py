# Items allowed for borrowing in this system.
ITEMS = ("Apple MacBook Pro",
         "ALFA Network AC1200 Wireless Adapter",
         "NVIDIA Jetson Nano Developer Kit",
         "Linksys WRT1900AC Dual-Band Wi-Fi Router",
         "DJI RoboMaster EP")

# Index represented in user item tuple inside key part in 
# user_borrow_record dictionary
INDEX_USER_BORROW_RECORD = 0
INDEX_ITEM_BORROW_RECORD = 1

def main():
    user_borrow_record = dict()
    while True:
        # Your Implementation starts here
        ###################################################
        print("Item(s) in stock:")
        # Display Item(s) menu for user selection
        print("Item No. | Item Name")
        for i in range(len(ITEMS)):
            print("       "+str(i)+".|",ITEMS[i])

        # ask input from user
        input_item_no=input("Please input the item no. to borrow (0 – 4):")
        input_quantity=int(input("Please input the quantity to borrow:"))
        input_borrower_name=input("Please input borrower's name:")
        print("")
        # create the key used in dictionary
        key = (input_borrower_name, input_item_no)
        
        # assign corresponding value for corresponding key
        user_borrow_record[key] = user_borrow_record.get(key,0) + input_quantity
        
        # display all records
        print("Item(s) Borrowers had borrowed:")
        print("Item No. | Item Name                                  | Borrower   | Qty. Borrowed")
        for key,borrow_quantity in sorted(user_borrow_record.items(), key=lambda item:item[0][1], reverse=False):
            borrowr,borrowr_item_no=key
            print(str(borrowr_item_no).rjust(7)+". |",ITEMS[int(borrowr_item_no)].ljust(42),"|",borrowr.ljust(10),"|",str(borrow_quantity).rjust(13))
        print("")
            
if __name__ == "__main__":
    main()

