#!/usr/bin/python
import vendingMachine

x = vendingMachine.VendingMachine()
run = True

print(30 * '-')
print("   V E N D - O - M A T I C   ")
print(30 * '-')
print("Press X to Exit")
print("Press C to see Cash Balance")
print(30 * '-')

message = "INSERT COIN"

terminate = False
product_selected = False
selected_product = None
product_price = None

while not selected_product:
    print("")
    print(40 * "#")
    print("Choose a product")
    products = x.get_products()
    keys = list(products)
    for index in range(len(keys)):
        product = keys[index]
        print("{} + ${:0,.2f}".format(product, products[product]))
    print(40 * "#")
    print("")

    choice = input("Select product [A,O,B]: ")
    if choice == "A":
        selected_product = vendingMachine.APPLE
    if choice == "O":
        selected_product = vendingMachine.ORANGE
    if choice == "B":
        selected_product = vendingMachine.BANANA

while not terminate:
    print("")
    print(40 * "#")
    print(message)
    print(40 * "#")
    print("")

    choice = input("Input coin [N,D,Q,$]: ")

    if choice == "N":
        x.input_coin(vendingMachine.NICKEL)
    elif choice == "D":
        x.input_coin(vendingMachine.DIME)
    elif choice == "Q":
        x.input_coin(vendingMachine.QUARTER)
    elif choice == "$":
        x.input_coin(vendingMachine.DOLLAR)
    elif choice == "X":
        print("Exit")
        terminate = True
    else:
        print("Invalid coin. Try again...")

    if x.can_purchase(selected_product):
        print(x.purchase_product(selected_product))

    if x.get_coins_value() > 0:
        message = "${:0,.2f}".format(x.get_coins_value())
    else:
        message = "INSERT COIN"
