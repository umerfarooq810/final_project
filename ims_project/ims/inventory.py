
# ims/inventory.py

from ims.product import Product
from ims.auth_system import User

class InventoryManagementSystem:
    MINIMUM_STOCK_THRESHOLD = 5

    def __init__(self):
        self.users = {}  # Dictionary to store users
        self.products = {}  # Dictionary to store products

    def add_user(self, username, password, role):
        self.users[username] = User(username, password, role)

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.authenticate(password):
            return user
        else:
            raise ValueError("Invalid username or password")

    def add_product(self, user, product_id, name, category, price, stock_quantity):
        if user.role != "Admin":
            print("Permission denied. Only Admin can add products.")
            return
        if product_id in self.products:
            print("Product with this ID already exists.")
            return
        self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
        print("Product added successfully.")

    def edit_product(self, user, product_id, name = None, category = None, price = None, stock_quantity = None):
        if user.role != "Admin":
            print("Permission denied. Only Admin can edit products.")
            return
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return

        if name:
            product.name = name
        if category:
            product.category = category
        if price is not None:
            product.price = price
        if stock_quantity is not None:
            product.stock_quantity = stock_quantity
        print("Product updated successfully.")

    def delete_product(self, user, product_id):
        if user.role != "Admin":
            print("Permission denied. Only Admin can delete products.")
            return
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        for product_id, product in self.products.items():
            print(f"ID: ({product_id}) -- Name: ({product.name}) -- Category: ({product.category}) -- "
                  f"Price: (${product.price}) -- Stock: ({product.stock_quantity}) ")
            if product.stock_quantity < self.MINIMUM_STOCK_THRESHOLD:
                print(" - Low stock! Consider restocking.")

    def search_product(self, name = None, category = None):
        results = [product for product in self.products.values()
                   if (name and product.name == name) or (category and product.category == category)]
        if not results:
            print("No matching products found.")
            return
        for product in results:
            print(f"ID: ({product.product_id}) -- Name: ({product.name}) -- Category: ({product.category}) -- "
                  f"Price: (${product.price}) -- Stock: ({product.stock_quantity}) ")

    def adjust_stock(self, user, product_id, quantity):
        if user.role != "Admin":
            print("Permission denied. Only Admin can adjust stock levels.")
            return
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        product.update_stock(quantity)
        print("Stock adjusted successfully.")
