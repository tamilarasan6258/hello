from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    return "Hello World!"





# A class to represent a product
class Product:
    # A constructor to initialize the product attributes
    def __init__(self, id, name, price, stock):
        self.id = id # A unique identifier for the product
        self.name = name # The name of the product
        self.price = price # The price of the product per unit
        self.stock = stock # The number of units available in the store

    # A method to display the product details
    def show(self):
        print(f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}")

    # A method to update the stock after a sale or a purchase
    def update_stock(self, quantity):
        self.stock += quantity # Add or subtract the quantity from the stock

# A list to store the products
products = []

# A function to add a new product to the list
def add_product():
    # Get the product details from the user
    id = input("Enter the product ID: ")
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the product stock: "))

    # Create a product object with the given details
    product = Product(id, name, price, stock)

    # Append the product object to the list
    products.append(product)

    # Display a confirmation message
    print("Product added successfully!")

# A function to display all the products in the list
def show_products():
    # Check if the list is empty
    if len(products) == 0:
        # Display a message
        print("No products available!")
    else:
        # Display a header
        print("ID\tName\tPrice\tStock")

        # Loop through the list and display each product
        for product in products:
            print(f"{product.id}\t{product.name}\t{product.price}\t{product.stock}")

# A function to search for a product by ID or name
def search_product():
    # Get the search criteria from the user
    choice = input("Do you want to search by ID or name? ")

    # Check if the choice is ID
    if choice.lower() == "id":
        # Get the ID from the user
        id = input("Enter the product ID: ")

        # Loop through the list and find the product with the matching ID
        for product in products:
            if product.id == id:
                # Display the product details
                product.show()
                # Return from the function
                return

        # If no product is found, display a message
        print("No product found with the given ID!")

    # Check if the choice is name
    elif choice.lower() == "name":
        # Get the name from the user
        name = input("Enter the product name: ")

        # Loop through the list and find the product with the matching name
        for product in products:
            if product.name == name:
                # Display the product details
                product.show()
                # Return from the function
                return

        # If no product is found, display a message
        print("No product found with the given name!")

    # If the choice is invalid, display a message
    else:
        print("Invalid choice!")

# A function to sell a product and update the stock
def sell_product():
    # Get the product ID from the user
    id = input("Enter the product ID: ")

    # Loop through the list and find the product with the matching ID
    for product in products:
        if product.id == id:
            # Display the product details
            product.show()

            # Get the quantity to sell from the user
            quantity = int(input("Enter the quantity to sell: "))

            # Check if the quantity is valid
            if quantity > 0 and quantity <= product.stock:
                # Calculate the total amount
                amount = quantity * product.price

                # Display the bill
                print(f"Bill: {amount}")

                # Update the stock
                product.update_stock(-quantity)

                # Display a confirmation message
                print("Product sold successfully!")

                # Return from the function
                return

            # If the quantity is invalid, display a message
            else:
                print("Invalid quantity!")

    # If no product is found, display a message
    print("No product found with the given ID!")

# A function to purchase a product and update the stock
def purchase_product():
    # Get the product ID from the user
    id = input("Enter the product ID: ")

    # Loop through the list and find the product with the matching ID
    for product in products:
        if product.id == id:
            # Display the product details
            product.show()

            # Get the quantity to purchase from the user
            quantity = int(input("Enter the quantity to purchase: "))

            # Check if the quantity is valid
            if quantity > 0:
                # Update the stock
                product.update_stock(quantity)

                # Display a confirmation message
                print("Product purchased successfully!")

                # Return from the function
                return

            # If the quantity is invalid, display a message
            else:
                print("Invalid quantity!")

    # If no product is found, display a message
    print("No product found with the given ID!")

# A function to display the main menu and get the user's choice
def main_menu():
    # Display the menu options
    print("Welcome to the departmental store!")
    print("1. Add a product")
    print("2. Show all products")
    print("3. Search a product")
    print("4. Sell a product")
    print("5. Purchase a product")
    print("6. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Return the choice
    return choice

# A loop to run the program until the user chooses to exit
while True:
    # Get the user's choice from the main menu
    choice = main_menu()

    # Perform the corresponding action based on the choice
    if choice == 1:
        # Add a product
        add_product()
    elif choice == 2:
        # Show all products
        show_products()
    elif choice == 3:
        # Search a product
        search_product()
    elif choice == 4:
        # Sell a product
        sell_product()
    elif choice == 5:
        # Purchase a product
        purchase_product()
    elif choice == 6:
        # Exit the program
        print("Thank you for using the departmental store!")
        break
    else:
        # Invalid choice
        print("Invalid choice! Please try again.")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]

