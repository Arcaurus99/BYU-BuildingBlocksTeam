
productList = {}

def displayMenu():
    option = input("\n--- MENU ---\n"
        "1. Add\n"
        "2. Display\n"
        "3. Remove\n"
        "4. Compute\n"
        "5. Quit\n"
        "------------\n"
        "Insert the number of the option you choose: ")

    return option

def add():
    print("----- ADD -----")
    name_new_product = input("What item would you like to add? ")
    price_new_product = input(f"What is the price of '{name_new_product}'? ")
    productList[name_new_product] = price_new_product

def display():
    print("---- DISPLAY ----\n"
        "Product List ---")
    for key in productList:
        print(f'- {key}:\t$ {float(productList[key]):.2f}')
    print("----------------")
    input()

def remove():
    while True:
        print("---- REMOVE ----\n"
            "Product List ---")
        for key in productList:
            print(f'- {key}:\t$ {float(productList[key]):.2f}')
        print("-----------------")
        to_remove_product = input("What item would you like to remove? ")
        print()
        if to_remove_product in productList:
            productList.pop(to_remove_product)
            print("Item succesfully removed.")
            break
        else:
            print("That item doesn't exist. Try again.")

def compute():
    total = 0
    for key in productList:
        total += float(productList[key])
    print(f'TOTAL: $ {float(total):.2f}')

if __name__ == '__main__':
    print("\n-- SHOPPING CART --"
        "\nWelcome to the product list manager")

    while True:
        option = displayMenu()
        print()     # <br>

        if option == '1':
            add()
        elif option == '2':
            display()
        elif option == '3':
            remove()
        elif option == '4':
            compute()
        elif option == '5':
            break
