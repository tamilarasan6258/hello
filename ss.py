from flask import Flask, render_template

app = Flask(__name__)

# A class to represent a product
class Product:
    # A constructor to initialize the product attributes
    def __init__(self, id, name, price, stock):
        self.id = id  # A unique identifier for the product
        self.name = name  # The name of the product
        self.price = price  # The price of the product per unit
        self.stock = stock  # The number of units available in the store

    # A method to display the product details
    def show(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

    # A method to update the stock after a sale or a purchase
    def update_stock(self, quantity):
        self.stock += quantity  # Add or subtract the quantity from the stock

# A list to store the products
products = []

# Flask route to display products
@app.route("/")
def display_products():
    return render_template("products.html", products=products)

# Flask route to handle product addition
@app.route("/add_product")
def add_product():
    id = input("Enter the product ID: ")
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the product stock: "))

    product = Product(id, name, price, stock)
    products.append(product)

    return "Product added successfully!"

# Flask route to handle selling a product
@app.route("/sell_product")
def sell_product():
    id = input("Enter the product ID: ")

    for product in products:
        if product.id == id:
            product.show()
            quantity = int(input("Enter the quantity to sell: "))
            if 0 < quantity <= product.stock:
                amount = quantity * product.price
                product.update_stock(-quantity)
                return f"Bill: {amount}\nProduct sold successfully!"
            else:
                return "Invalid quantity!"

    return "No product found with the given ID!"

# Flask route to handle purchasing a product
@app.route("/purchase_product")
def purchase_product():
    id = input("Enter the product ID: ")

    for product in products:
        if product.id == id:
            product.show()
            quantity = int(input("Enter the quantity to purchase: "))
            if quantity > 0:
                product.update_stock(quantity)
                return "Product purchased successfully!"
            else:
                return "Invalid quantity!"

    return "No product found with the given ID!"

# Flask route to display the main menu
@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")

# Main entry point for the application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
