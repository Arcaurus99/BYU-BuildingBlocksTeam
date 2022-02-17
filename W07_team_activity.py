import random

flag_again = True

# ----- CORE REQUIREMENTS -----
def guessMyNumberGame():
    # var_magic_num = float(input("What is the magic number? "))
    var_attemp_count = 0
    var_magic_num = random.randint(1,100)
    while True:
        var_guess_num = int(input("What is your guess? "))
        var_attemp_count += 1
        if var_guess_num == var_magic_num:
            print('-------------------------\n'
                'Congrats! You guessed it!\n'
                f"The magic number was: {var_guess_num}\n"
                f"Number of attemps: {var_attemp_count}\n"
                '-------------------------\n')
            break
        elif var_guess_num <= var_magic_num:
            print('Higuer')
        elif var_guess_num >= var_magic_num:
            print('Lower')
        else:
            print('default')



if __name__ == '__main__':
    print('------- WELCOME TO --------\n'
        '--- GUES THE NUMER GAME ---\n')
    while flag_again:
        print('The Magic Number was setted.\n'
            'Try to guess it. Good luck!\n')
        guessMyNumberGame()

        while True:
            var_if_again = input("Do you want to play again (yes/no)? ")
            if var_if_again.lower() == 'yes':
                input('Here we going again...   (Press Enter to continue.)\n')
                break
            elif var_if_again.lower() == 'no':
                print('Bye!\n')
                flag_again = False
                break
            else:
                print("I don't understand. Try again! \n")
        
