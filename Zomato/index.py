import json

# Function to load menu and orders data from files
def load_data():
    try:
        with open("menu.json", "r") as menu_file:
            menu_data = json.load(menu_file)
    except (FileNotFoundError, json.JSONDecodeError):
        menu_data = {}
    
    try:
        with open("orders.json", "r") as orders_file:
            orders_data = json.load(orders_file)
    except (FileNotFoundError, json.JSONDecodeError):
        orders_data = {}
    
    return menu_data, orders_data


# Function to save menu and orders data to files
def save_data(menu_data, orders_data):
    with open("menu.json", "w") as menu_file:
        json.dump(menu_data, menu_file, indent=4)
    
    with open("orders.json", "w") as orders_file:
        json.dump(orders_data, orders_file, indent=4)

# Function to display the menu
def display_menu(menu_data):
    print("==== Zesty Zomato Menu ====")
    print("ID  | Dish Name              | Price     | Availability")
    print("-----------------------------------------------------")
    for dish_id, dish_info in menu_data.items():
        print(f"{dish_id:<4} | {dish_info['name']:<22} | {dish_info['price']:<9} | {dish_info['availability']}")
    print()

# Function to add a new dish to the menu
def add_dish(menu_data):
    dish_id = input("Enter the dish ID: ")
    if dish_id in menu_data:
        print("Error: Dish with this ID already exists.")
        return
    
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ").lower() == 'yes'
    
    menu_data[dish_id] = {
        'name': dish_name,
        'price': price,
        'availability': availability
    }
    print(f"Dish '{dish_name}' has been added to the menu.\n")

# Function to remove a dish from the menu
def remove_dish(menu_data):
    dish_id = input("Enter the dish ID to remove: ")
    if dish_id not in menu_data:
        print("Error: Dish with this ID does not exist.")
        return
    
    dish_name = menu_data[dish_id]['name']
    del menu_data[dish_id]
    print(f"Dish '{dish_name}' has been removed from the menu.\n")

# Function to update the availability of a dish
def update_availability(menu_data):
    dish_id = input("Enter the dish ID to update availability: ")
    if dish_id not in menu_data:
        print("Error: Dish with this ID does not exist.")
        return
    
    availability = input("Is the dish available? (yes/no): ").lower() == 'yes'
    menu_data[dish_id]['availability'] = availability
    print("Availability updated.\n")

# Function to take a new order
def take_order(menu_data, orders_data):
    customer_name = input("Enter customer name: ")
    order_dishes = input("Enter dish IDs (comma-separated): ").split(",")

    total_price = 0
    for dish_id in order_dishes:
        if dish_id in menu_data and menu_data[dish_id]['availability']:
            total_price += menu_data[dish_id]['price']
        else:
            print(f"Error: Dish with ID {dish_id} is not available in the menu.")
            return

    order_id = str(len(orders_data) + 1)
    orders_data[order_id] = {
        'customer_name': customer_name,
        'order_dishes': order_dishes,
        'status': 'received',
        'total_price': total_price
    }

    print(f"Order ID: {order_id}")
    print(f"Total Price: {total_price:.2f}\n")

# Function to update the status of an order
def update_order_status(orders_data):
    order_id = input("Enter the order ID to update status: ")
    if order_id not in orders_data:
        print("Error: Order with this ID does not exist.")
        return
    
    new_status = input("Enter the new status: ")
    orders_data[order_id]['status'] = new_status
    print("Order status updated.\n")

# Function to review all orders
def review_orders(orders_data):
    print("==== All Orders ====")
    status_filter = input("Enter status to filter (leave empty for all orders): ").lower()

    for order_id, order_info in orders_data.items():
        if not status_filter or order_info['status'].lower() == status_filter:
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {order_info['customer_name']}")
            print(f"Dishes: {', '.join(order_info['order_dishes'])}")
            print(f"Status: {order_info['status']}")
            if 'total_price' in order_info:
                print(f"Total Price: {order_info['total_price']:.2f}")
            print("---------------")
    print()

# Main function to start the Zesty Zomato system
def main():
    menu_data, orders_data = load_data()

    while True:
        print("==== Zesty Zomato: The Great Food Fiasco ====")
        print("1. Display Menu")
        print("2. Add New Dish")
        print("3. Remove Dish")
        print("4. Update Dish Availability")
        print("5. Take New Order")
        print("6. Update Order Status")
        print("7. Review All Orders")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_menu(menu_data)
        elif choice == '2':
            add_dish(menu_data)
        elif choice == '3':
            remove_dish(menu_data)
        elif choice == '4':
            update_availability(menu_data)
        elif choice == '5':
            take_order(menu_data, orders_data)
        elif choice == '6':
            update_order_status(orders_data)
        elif choice == '7':
            review_orders(orders_data)
        elif choice == '8':
            save_data(menu_data, orders_data)
            print("Thank you for using Zesty Zomato. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
