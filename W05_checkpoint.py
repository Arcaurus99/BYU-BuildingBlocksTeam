def numberComparison():
    first_num = int(input("Insert a number: "))
    second_num = int(input("Insert a second number: "))

    # --- FIRST NUMBER ---
    if first_num > second_num:
        print(f"The first number is greater than the second. ({first_num} > {second_num})")
    else:
        print(f"The first number is not greater than the second. ({first_num} < {second_num})")

    # --- EQUALITY ---
    if first_num == second_num:
        print(f"The numbers are equal. ({first_num} = {second_num})")
    else:
        print(f"The numbers are not equal. ({first_num} != {second_num})")

    # --- SECOND NUMBER ---
    if first_num < second_num:
        print(f"The second number is greater than the first. ({second_num} > {first_num})")
    else:
        print(f"The second number is not greater than the first. ({second_num} < {first_num})\n")

def favAnimalComparison():
    fav_animal = input("What is your favorite animal? \n- ")
    if fav_animal.lower() == 'bear':
        print(f"The {fav_animal}?! That's my favorite animal too!")
    else:
        print(f"The {fav_animal}? Hum... that one is not my favorite animal.\n")

if __name__ == '__main__':
    favAnimalComparison()
    