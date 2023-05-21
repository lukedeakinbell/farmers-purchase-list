


#Below is the function to display the main menu options
def display_main_menu():
    print("Welcome to Luke's Farmer's Market!")
    print("1. Quit")
    print("2. Admin Login")
    print("3. Buy Produce")

#Function to handle the buy product option
def buy_product(products):
    print("Lukes Farmer Produce List:")
    for product, price in products.items():
        print(f"{product}: ${price:.2f}")
#function is used to convert the user input, which is initially a string, into an integer data type. 
    print("To order your product, enter the exact product name followed by the quantity.")
    product_name = input("Enter name of your desired produce: ")
    quantity = int(input("Enter quantity: "))


#using if statement to include the product name and multiply it be the selected quantity

    if product_name in products:
        total_price = products[product_name] * quantity
        print(f"Total Price: ${total_price:.2f}")
        confirm = input("Confirm purchase? (yes/no): ")

        if confirm.lower() == "yes":
            print("Purchase order confirmed, thanks for shopping.")
        else:
            print("Order cancelled.")
    else:
        print("Invalid product name.")

# Function to handle the admin login option
def admin_login(products):
    username = input("Enter username: ")
    password = input("Enter password: ")

    #This step Validates the correct username and password
    #I've opted to use a simple password and username as the data structure
    if username == "admin" and password == "password":
        print("ADMIN OPTIONS:")
        print("1. Quit")
        print("2. Main Menu")
        print("3. Add/Update/Delete Product")
        admin_option = input("Enter option: ")

        if admin_option == "1":
            print("The program has ended.")
        elif admin_option == "2":
            print("Returning to the main menu.")
        elif admin_option == "3":
            add_update_delete_product(products)
        else:
            print("Invalid option.")
    else:
        print("Invalid username or password.")

# Function to add, update, or delete a product
def add_update_delete_product(products):
    print("ADD/UPDATE/DELETE Produce:")
    print("1. Add Produce")
    print("2. Update Product")
    print("3. Delete Product")
    admin_choice = input("Enter choice: ")

    if admin_choice == "1":
        name = input("Enter produce name: ")
        price = float(input("Enter produce price: "))
        products[name] = price
        # Add the new product to the existing product list
        print("Produce added successfully.")
    elif admin_choice == "2":
        product_name = input("Enter produce name to update: ")
        if product_name in products:
            new_price = float(input("Enter new produce price: "))
            products[product_name] = new_price
            print("Produce updated successfully.")
        else:
            print("Invalid product name.")
    elif admin_choice == "3":
        product_name = input("Enter produce name to delete: ")
        if product_name in products:
            del products[product_name]
            print("produce deleted successfully.")
        else:
            print("Invalid name.")
    else:
        print("Invalid choice.")

# Main program loop
products = {
    "Banana": 0.75,
    "Strawberry": 1.25,
    "Eggs": 2.5,
    "Cheese": 3.0,
    "Milk": 2.0
}

while True:
    display_main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Program quite, goodbye")
        break
    elif choice == "2":
        admin_login(products)
    elif choice == "3":
        buy_product(products)
    else:
        print("Invalid choice. Please try again.")



