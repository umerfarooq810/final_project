

# ims/main.py

from ims.inventory import InventoryManagementSystem

# Sample data setup
ims = InventoryManagementSystem()
ims.add_user("admin", "pass123", "Admin")
ims.add_user("user", "pass123", "User")

# Console menu for system interaction
def main_menu():
    print("\nInventory Management System")
    print("1. Login")
    print("2. Exit\n")

def admin_menu():
    print("\nAdmin Menu")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View All Products")
    print("5. Search Product")
    print("6. Adjust Stock")
    print("7. Logout\n")

def user_menu():
    print("\nUser Menu")
    print("1. View All Products")
    print("2. Search Product")
    print("3. Logout\n")

# Main program loop
current_user = None
while True:
    if not current_user:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                current_user = ims.login(username, password)
                print(f"Welcome, {current_user.username}!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            print("Exiting the system...\n")
            break
    else:
        if current_user.role == "Admin":
            admin_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                stock_quantity = int(input("Stock Quantity: "))
                ims.add_product(current_user, product_id, name, category, price, stock_quantity)
            elif choice == "2":
                product_id = input("Product ID to edit: ")
                name = input("New Name (leave blank to skip): ")
                category = input("New Category (leave blank to skip): ")
                price = input("New Price (leave blank to skip): ")
                stock_quantity = input("New Stock Quantity (leave blank to skip): ")
                ims.edit_product(current_user, product_id, name or None, category or None,
                                 float(price) if price else None,
                                 int(stock_quantity) if stock_quantity else None)
            elif choice == "3":
                product_id = input("Product ID to delete: ")
                ims.delete_product(current_user, product_id)
            elif choice == "4":
                ims.view_products()
            elif choice == "5":
                name = input("Search by name (leave blank to skip): ")
                category = input("Search by category (leave blank to skip): ")
                ims.search_product(name or None, category or None)
            elif choice == "6":
                product_id = input("Product ID to adjust stock: ")
                print("(+plus) 1,2,3,.... --- (-minus) -1,-2,-3,....")
                quantity = int(input("Quantity (positive to add, negative to reduce): "))
                ims.adjust_stock(current_user, product_id, quantity)
            elif choice == "7":
                current_user = None
                print("Logged out...")
        elif current_user.role == "User":
            user_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                ims.view_products()
            elif choice == "2":
                name = input("Search by name (leave blank to skip): ")
                category = input("Search by category (leave blank to skip): ")
                ims.search_product(name or None, category or None)
            elif choice == "3":
                current_user = None
                print("Logged out...")
