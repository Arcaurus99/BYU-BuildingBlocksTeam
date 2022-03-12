
bank_account_list = []
bank_balance_list = []

def add():
    while True:
        new_account = input("What is the name of this account? ")
        if new_account.lower() != 'quit':
            new_balance = float(input("What is the balance? "))
            bank_account_list.append(new_account)
            bank_balance_list.append(new_balance)
        else:
            break
                    
def displayListAndData():
    total = 0
    id = 0
    print("\nAccount Information:")
    for i in range(len(bank_account_list)):
        print(f"{id}. {bank_account_list[i]} - ${bank_balance_list[i]:.2f}")
        total += bank_balance_list[i]
        id += 1

    print(f"\nTotal: ${total:.2f}")
    average = total / len(bank_balance_list)
    print(f"Average: ${average:.2f}")

def highestBalance():
    highestBalanceAccount = ''
    highestBalanceValue = 0
    for i in range(len(bank_account_list)):
        if highestBalanceValue < bank_balance_list[i]:
            highestBalanceAccount = bank_account_list[i]
            highestBalanceValue = bank_balance_list[i]
    print(f"Highest balance: {highestBalanceAccount} - ${highestBalanceValue:.2f}")

def update():
    while True:
        flag = input("\nDo you want to update an account (yes/no)? ")
        if flag == 'yes':
            id_account = int(input("What account index do you want to update? "))
            amount = float(input("What is the new amount? "))
            bank_balance_list[id_account] = amount
            displayListAndData()  
        elif flag == 'no':
            break


if __name__ == '__main__':
    print("\nEnter the names and balances of bank accounts (type: quit when done)\n")    
    add()
    displayListAndData()
    highestBalance()
    update()