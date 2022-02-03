
def firstChoice():
    print("")
    while True:
        var_select = input("¿Do you want to SLEEP again or GET UP and go to bathroom? (Type your selected action as exactly verb is ia) \n> ")
        if var_select == 'SLEEP':
            options1(var_select)
        elif var_select == 'LEVANTARTE':
            break

def options1(select):
    print("You roll over and fall asleep. When you wake up again it's 7:00 am, you get up and rum to get ready quickly,")
    while True:
        select = input("¿Do you want to SLEEP again or GET UP and go to bathroom? (Type your selected action) \n> ")
        if select == 'TAKE A BATH':
            print(select)
        elif select == 'EAT BREAKFAST':
            print(select)
        else:
            print("There is no option for the action {select}. \nTry again and type the action you select")

if __name__ == '__main__':
    print("-------- History Game --------")
    firstChoice()