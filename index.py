import json

# Function to load menu from a JSON file
def load_menu():
    try:
        with open("menu.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save menu to a JSON file
def save_menu(menu):
    with open("menu.json", "w") as file:
        json.dump(menu, file)

# Function to load orders from a JSON file
def load_orders():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save orders to a JSON file
def save_orders(orders):
    with open("orders.json", "w") as file:
        json.dump(orders, file)

# Function to display the menu
def display_menu(menu):
    print("\nMenu of Zesty Zomato:")
    print("------------------------------------------------------")
    print("| {:^8} | {:^15} | {:^6} | {:^11} |".format("Dish ID", "Dish Name", "Price", "Availability"))
    print("------------------------------------------------------")
    for dish in menu:
        dish_id, dish_name, price, available = dish
        availability = "Yes" if available else "No"
        print("| {:^8} | {:^15} | {:^6.2f} | {:^11} |".format(dish_id, dish_name, price, availability))
    print("------------------------------------------------------")


# Function to add a new dish to the menu
def add_dish(menu):
    dish_id = int(input("Enter the Dish ID: "))
    dish_name = input("Enter the Dish Name: ")
    price = float(input("Enter the Price: "))
    available = input("Is the Dish available? (yes/no): ").lower() == "yes"
    menu.append((dish_id, dish_name, price, available))
    save_menu(menu)
    print("Dish added to the menu.")

# Function to remove a dish from the menu
def remove_dish(menu):
    dish_id = int(input("Enter the Dish ID to remove: "))
    for dish in menu:
        if dish[0] == dish_id:
            menu.remove(dish)
            save_menu(menu)
            print("Dish removed from the menu.")
            return
    print("Dish not found.")

# Function to update the availability of a dish
def update_availability(menu):
    dish_id = int(input("Enter the Dish ID to update availability: "))
    for dish in menu:
        if dish[0] == dish_id:
            available = input("Is the Dish available? (yes/no): ").lower() == "yes"
            dish[3] = available
            save_menu(menu)
            print("Availability updated.")
            return
    print("Dish not found.")

# Function to take a new order
def take_order(menu, orders):
    customer_name = input("Enter the customer's name: ")
    order_items = input("Enter the Dish IDs (comma-separated): ").split(",")
    order = {
        "order_id": len(orders) + 1,
        "customer_name": customer_name,
        "items": order_items,
        "status": "received"
    }
    orders.append(order)
    save_orders(orders)
    print("Order placed successfully.")

# Function to update the status of an order
def update_order_status(orders):
    order_id = int(input("Enter the Order ID to update status: "))
    for order in orders:
        if order["order_id"] == order_id:
            new_status = input("Enter the new status (received/preparing/ready): ")
            order["status"] = new_status
            save_orders(orders)
            print("Order status updated.")
            return
    print("Order not found.")

# Function to display all orders
def display_orders(orders, menu):
    print("\nAll Orders:")
    print("--------------------------------------------------------------------------------------------------------")
    print("| {:^10} | {:^20} | {:^25} | {:^15} | {:^15} |".format("Order ID", "Customer Name", "Items", "Total Price","Status"))
    print("--------------------------------------------------------------------------------------------------------")
    for order in orders:
        order_id = order["order_id"]
        customer_name = order["customer_name"]
        status = order["status"]
        items = []
        total_price = 0
        for item_id in order["items"]:
            for dish in menu:
                if dish[0] == int(item_id):
                    _, dish_name, price, _ = dish
                    items.append(dish_name)
                    total_price += price
                    break
        items_str = ", ".join(items)
        print("| {:^10} | {:^20} | {:^25} | {:^15.2f} | {:^15} |".format(order_id, customer_name, items_str, total_price, status))
    print("--------------------------------------------------------------------------------------------------------")


# Main function to run the application
def main():
    menu = load_menu()
    orders = load_orders()
    while True:
        print("\n===== Zesty Zomato Food Delivery System =====")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Display All Orders")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_dish(menu)
        elif choice == "3":
            remove_dish(menu)
        elif choice == "4":
            update_availability(menu)
        elif choice == "5":
            take_order(menu, orders)
        elif choice == "6":
            update_order_status(orders)
        elif choice == "7":
            display_orders(orders,menu)
        elif choice == "8":
            print("\nThank You !!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()