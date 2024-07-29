# Define the menu of restaurant
menu = {
    'Pizza':100,
    'Pasta':50,
    'Burger':60,
    'Girlic Bread':40,
    'Coffee':80
}
# Greet
print(" Welcom To Python Resturent ")
print("Pizza: Rs100\nPasta: Rs50\nBurger: Rs60\nGirlic Bread: Rs40\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter the name if item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item {item_1} has been added to your order")

else:
    print(f"Ordered itme {item_1} is not avaialable yet")

another_order = input("Do you want to add another item?(yes/nO)")  
if another_order == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2} is not avaialable!")

print(f"The total amount of item to pay is {order_total}")     


