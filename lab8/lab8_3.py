INDEX_QUANTITY = 0
INDEX_TOTAL_SALES = 1
def main():
    products = dict()
    print ("Welcome to product selling system")
    while True:
        name = input("Input product name: ").lower()
        price = float(input("Input selling price for current order: "))
        quantity = int(input("Input quantity for current order: "))

        # your code goes here
        
        products[name]={INDEX_QUANTITY:price,INDEX_TOTAL_SALES:quantity}
        print("Statistics of product selling")
        print(products)
        for product in products.items():
            product_name,product_index=product
            product_price=product_index[INDEX_QUANTITY]
            product_quantity=product_index[INDEX_TOTAL_SALES]
            
            print("Item:",product_name,"- Quantity sold:",product_quantity,"- Total sales amount:",product_quantity*product_price)
        


# You are not allowed to modify the following codes
if __name__ == "__main__":
    main()
