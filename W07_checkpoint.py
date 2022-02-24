
import string


def checkPositiveNumber():
    while True:
        var_num_input = float(input("Please type a positive number: "))
        if var_num_input >= 0:
            print(f"The number is: {var_num_input:.0f}")
            break
        else:
            print('Sorry, that is a negative number. Please try again.')

def candyRequest():
    while True:
        var_if_candy = input("May I have a piece of candy? ")
        if var_if_candy.lower() == 'yes':
            print('Thank you.')
            break

if __name__ == '__main__':
    # checkPositiveNumber()
    candyRequest()