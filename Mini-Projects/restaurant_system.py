# define the menu of the restaurant

#Python basics
#Dictionaries
#if-else
#User input
#Simple billing logic
#Mini project structure
menu = {
    'Pizza': 149,
    'Pasta': 139,
    'Burger': 129,
    'Salad': 59,
    'Coffee': 189,
}

# greet
print("Welcome to the Python Cafe")
print("Pizza: Rs 149\nPasta: Rs 139\nBurger: Rs 129\nSalad: Rs 59\nCoffee: Rs 189\n")

order_total = 0

# first item
item_1 = input("Enter the name of the item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

# ask for another item
another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of items is Rs {order_total}")