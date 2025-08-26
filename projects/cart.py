import pandas as pd
from prettytable import PrettyTable
import datetime
import os
import sys
import ast #abstract syntax trees (safely read and understand Python code stored as text.)

def logout(): pass
def login(): pass
def viewProducts(): pass
def run(): pass
def signup(): pass
def initial(): pass
def viewCart(): pass
def confirmOrder(): pass
def orderHistory(): pass

orderId=0
custName=[] #
orderDf= pd.read_excel("cart_data.xlsx")
if orderDf.empty or "ID" not in orderDf.columns:
    orderId=1
else:
     orderId = orderDf["ID"].iloc[-1] +1
    
productName=[] #
productQty=[] #
totalPrice=0 #
orderDate=[] #
orderTime=[] #


def breakingCode():
    print("==Exited Successfully==")
    sys.exit()


def signUp():
    print("="*25)
    print("CREATING YOUR ACCOUNT...🔃")
    name = input("Enter name: ")
    if not name:
        print("Name can't  be empty.")
        signUp()
    password = input("Enter password: ")
    if not password:
        print("Password can't  be empty.")
        signUp()
 
    with open("users.txt", "r") as file1:
        for line in file1:
            parts= line.strip().split(",")
            if name==parts[0]:
                print("Username already exists")
                print("USE ANOTHER USERNAME")
                signUp()

    with open("users.txt", "a") as file:
        file.write(f'{name},{password} \n')
            



  

    print("Account Created successfully!🎉 ")
    print("="*25)
    while True:
        print("1) Login \n2)Main Menu")
        userInput=input()
        if userInput == "1":
            login()
        elif userInput =="2":
            initial()
        else:
            print("Invalid Input, Try Again.")
            continue


def login():
    name = input("Enter name: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as file:
        for line in file:
            username, userPassword = line.strip().split(",")
            if username == name and userPassword==password:
                print("==Login successfully==")
                print("="*25)
                custName.append(name)
                run()
                break
        else:
            print("Invalid input details")
            login()

def viewCart(user):
    
    df= pd.read_excel("cart_data.xlsx")
    cstName= df[df["Customer Name"].str.contains(user, case=True)]
    if cstName.empty:

        print("——Your 🛒 cart is empty——")

    
    else:
        print("This is your cart. ")
        print(cstName.to_string(index=False))
        print("-"*40)
        print("What you want: ")
        print("1. Confirm Order: ")
        print("2. Back to Menu: ")
        choiceInput=input("→")
        if choiceInput=="1":
            userInput=int(input("Select id to confirm order: "))
            # orderConfirm=df[df["ID"] == userInput]
            print("Order confirmed successfully. ")
            file1=pd.read_excel("cart_data.xlsx")
            file2=pd.read_excel("orderHistory.xlsx")
            ordered_prouct = file1[file1["ID"]==userInput]
            file1=file1[file1["ID"]!=userInput]
            file2=pd.concat([file2,ordered_prouct],ignore_index=True)
            file1.to_excel("cart_data.xlsx",index=False)
            file2.to_excel("orderHistory.xlsx",index=False)
            print("Do you want to order more items (y/n)")
            userConfirmation= input().lower()
            try:
                if userConfirmation== "y":
                    viewCart(custName[0])
                elif userConfirmation =="n":
                    run()
            except ValueError:
                print(ValueError)

        elif choiceInput =="2":
            run()  
        else:
            print("Wrong Input")


    run()
    
    
def run():
    print("Select option: ")
    print("1) View Items ")
    print("2) View cart: ")
    print("3) Order History: ")
    print("4) My account")
    print("5) Logout")
    print("6) Exit Program")
    store = input()

    if store=="1":
        viewProducts()
    elif store=="2":
        viewCart(custName[0])
    elif store=="3":
        orderHistory()
    elif store=="4":
        myAccount()
    elif store=="5":
        logout()
    elif store=="6":
        breakingCode()
    else:
        print("Wrong input, Try Again.")
        run()

 
def logout():
    """Clear all user-specific data"""
    global custName, productName, productQty, totalPrice, orderDate, orderTime
    
    # Reset all user-related variables
    custName=[] #
    productName=[] #
    productQty=[] #
    totalPrice=0 #
    orderDate=[] #
    orderTime=[] #
        
    print("Successfully logged out!")
    print("=" * 40)
    initial()


def viewProducts():
    productName.clear()
    productQty.clear()
    totalPrice=0

    cartProduct={}

    df = pd.read_excel("products.xlsx")  

    orderDetails = {
    "orderName": df["orderName"].tolist(),
    "orderPrice": df["orderPrice"].tolist(),
    "orderId": df["orderId"].tolist()
    }

    for i in range(len(orderDetails["orderId"])):
        print(" ID:",orderDetails["orderId"][i], ","
        " Product:", orderDetails["orderName"][i], "," 
        " Price:",orderDetails["orderPrice"][i])
    print("-"*40)
    n=0
    while True:

        orderName = input("Select product Name: ")
        if orderName not in orderDetails["orderName"]:
            print("❌ Invalid product, try again.")
            continue
        qty=None
        while qty is None:
            try:
                qty_input= int(input("Enter the qty: "))
                if qty_input <= 0:
                    print("Error, Qty must be greater than 0")
                else:
                    qty=qty_input
            except ValueError:
                print("Wrong input, try again")


        productQty.append(qty)

        indexOfOrder = orderDetails["orderName"].index(orderName)

        priceOfOrders=orderDetails["orderPrice"][indexOfOrder] * qty
        nameOfOrder=orderDetails["orderName"][indexOfOrder] 
        totalPrice+=priceOfOrders
        cartProduct[n] = {
            "name": nameOfOrder+f' ({qty})',
            "price": priceOfOrders,
            "id": orderDetails["orderId"][indexOfOrder]
        }
        productName.append(nameOfOrder)

        n += 1
        YesNo = input("Do you want to add one more item (Y/N): ").lower()
        if YesNo != "y":
            break

    checkoutInput = input('Press "p" to proceed or "m" to menu: ').lower()
    if checkoutInput == "p":
        table = PrettyTable()
        table.field_names = ["Product Name", "Price", "ID"]
        priceTol=0
        for product in cartProduct.values():
            table.add_row([product["name"], product["price"], product["id"]])
            priceTol+=product["price"]

        print("\n🛒 You ordered:")
        print(table)
        print("total Price:",priceTol )

        print("What to do now: ")
        print("1) Add to Cart ")
        print("2) Dismiss ")

        confirmation=input()
        while True:
            if confirmation=="1":
                # print(f'Thank You {custName[0]} 🎉🎉🎉🎉\nOrder Placed successfully at:{datetime.datetime.now().time()}')
                orderDate = datetime.date.today().strftime("%Y-%m-%d")  # Format: "2025-08-20"
                orderTime = datetime.datetime.now().strftime("%H:%M:%S")  # Format: "14:30:45"
                print("Added to cart")
                # global orderId
                # orderId+=1
                storeUserOrder={
                    "ID":orderId,
                    "Customer Name":custName[0],
                    "Product Name":productName,
                    "Qty":productQty,
                    "Price":totalPrice,
                    "Date":orderDate,
                    "Time":orderTime
                    
                }

                
                df= pd.DataFrame([storeUserOrder])
                existing_df = pd.read_excel("cart_data.xlsx")
                combined_df= pd.concat([existing_df, df], ignore_index=True)
                combined_df.to_excel("cart_data.xlsx", index=False)

            
                    
                print("="*40)
                run()
    

            elif confirmation=="2":
                print("Order dismissed ❌❌")
                run()
            else:
                print("Invalid input")
                continue


        else:
            print("Running")
            run()

def orderHistory():
    print("These are your order details 📃")
    global custName
    file1=pd.read_excel("orderHistory.xlsx")
    print(custName)
    custName= file1[file1["Customer Name"].str.contains(custName[0], case=True)]
    if custName.empty:
        print("empty")
    else:
        print(custName)

        print("="*20)
        all_items = []

        for cell in file1["Product Name"]:
            if pd.notna(cell):  # ignore empty cells
                items = ast.literal_eval(cell)  # convert string → real Python list
                all_items.extend(items)         # add items to final list
        print(f"You ordered {len(all_items)} items till now")
        

def myAccount():
    print("Your account details: ")
def initial():
    print("What you want to do: ")
    print("1) Login")
    print("2) Signup")
    print("3) Exit program")
    userInput=input()
    if userInput=="1":
        login()
    elif userInput=="2":
        signUp()
    elif userInput=="3":
        breakingCode()
    else:
        print("wrong input, Try again")
        initial()
initial()

