
def mealPriceCalculator():
    print("------ MEAL PRICE CALCULATOR ------\n")
    
    var_tip = 0
    var_total = 0

    var_child_meal = float(input("Insert the price of a child's meal: "))
    var_adult_meal = float(input("Insert the price of an adult's meal: "))
    var_child_drink = float(input("Insert the price of a child's drink: "))
    var_adult_drink = float(input("Insert the price of an adult's drink: "))
    var_child_num = int(input("Insert the number of children: "))
    var_adult_num = int(input("Insert the number of adults: "))
    var_tax_rate = float(input("Insert the sales tax rate: "))

    print("\n")         # <br> :D

    var_child_total = (var_child_meal * var_child_num) + (var_child_drink * var_child_num)
    var_adult_total = (var_adult_meal * var_adult_num) + (var_adult_drink * var_adult_num)
    var_subtotal = var_child_total + var_adult_total
    print(f"Subtotal: ${round(var_subtotal, 2)}")        # Other way to give format "{:.2f}".format(a_float)

    var_sales_tax = var_subtotal * (var_tax_rate / 100)
    print(f"Sales Tax: ${round(var_sales_tax, 2)}")
    
    # Calculating total / With or without tip
    var_total = var_subtotal + var_sales_tax
    var_tip = tip()         # Calling tip function
    print(var_tip)
    if var_tip != 0:
        var_total += var_tip
    print(f"\nTotal: ${round(var_total, 2)}\n")

    # Calculating payment
    pay(var_total)

# Tip function
def tip():
    while True:
        tip_flag = input("\n"
            "Do you want to give a tip?\n"
            "[1] Yes\n"
            "[2] No\n"
            "Insert the number of your option: ")           # The option is saved as a char
        if tip_flag == '1':
            var_tip_amount = int(input("Insert the payment amount: "))
            return var_tip_amount
            break
        elif tip_flag == '2':
            return 0
            break
        else:
            print(f"{tip_flag} there isn't a valid option, please try again.\n")

# Pay function
def pay(var_total):
    while True:
        var_pay_amount = int(input("Insert the payment amount: "))
        if var_pay_amount < var_total:
            print(f"{var_pay_amount} isn't enough.")
            print(f"\nTotal: ${round(var_total, 2)}")        # Other way to give format "{:.2f}".format(a_float)
        else:
            var_change = var_pay_amount - var_total
            print(f"Change: ${round(var_change, 2)}\n"
                "-----------------------------------\n\n")
            break

while True:
    print("\n------------ WELCOME TO -----------")
    mealPriceCalculator()

    flag = input(
        "Do you want to calculate a meal again?\n"
        "[1] Yes\n"
        "[2] No\n"
        "Insert the number of your option: ")
    if flag == '1':
        print("\nloading...")
    elif flag == '2':
        print(f"\nThanks for choosing us! \nCome back soon!"
            "\n--------------- BYE ---------------"
            "\n-----------------------------------")
        break
    else:
        print(f"{flag} there isn't a valid option, please try again.\n")
