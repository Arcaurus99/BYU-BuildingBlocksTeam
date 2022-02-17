
def firstChoice(first_start):
    if first_start == True:
        print("You wake up, you are in the floor, then look your watch and it's 5:00 am.")
        first_start = False
    else:
        print("You wake up, you are in the floor, you fell of the bed... You look your watch and it's 5:00 am.")

    while True:
        first_choice_input = input("¿Do you want to SLEEP again or GET UP and go to bathroom? (Type the verb you select as your choice, those who are in uppercase.) \n> ")
        options1(first_choice_input)       # FUNC OPTION 1

def options1(choice_input):
    print("")
    if choice_input.upper() == 'SLEEP':
        print("You roll over and fall asleep. When you wake up again it's 7:00 am, you get up and start to get ready")
        while True:
            new_choice_input = input("¿Do you want to TAKE A BATH, EAT your breakfast or CHECK your phone? \n> ")
            options2(new_choice_input)       # FUNC OPTION 2
    elif choice_input.upper() == 'GET UP':
        print("You go to the bathroom and wash your face, you return to the room when your cell phone makes a sound indicating an incoming notification. A message from your best friend inviting you to go see the sunrise over the hill at the ends of the city.")
        while True:
            new_choice_input = input("¿Do you want to GET READY to go with him or REFUSE the invitation? \n> ")
            options3(new_choice_input)       # FUNC OPTION 3
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")
    

def options2(choice_input):
    print("")
    if choice_input.upper() == 'TAKE A BATH':
        print("While you was in the bath you feel the floor is shaking. It's an earthquake!")
        while True:
            new_choice_input = input("You live on the tenth floor of an apartment building. Do you want to RUN, HIDE or just KEEP CALM? \n> ")
            options4(new_choice_input)       # FUNC OPTION 4
    elif choice_input.upper() == 'EAT':
        print("While you was preparing your cocoa, you feel the floor is moving. It's an earthquake!")
        while True:
            new_choice_input = input("You live in the tenth floor of an apartment building. Do you want to RUN, HIDE or just KEEP CALM? \n> ")
            options4(new_choice_input)       # FUNC OPTION 4
    elif choice_input.upper() == 'CHECK':
        print("You are looking the news and see that many natural disasters are happening around the world, you see something through the window, and jump out of bed to see better, suddenly the floor shakes, it's an earthquake! The window shatters and with a violent jolt throws you out of the building.")
        flap_times = 0
        while True:
            new_choice_input = input("You want to FLAP your arms or just CLOSE your eyes.? \n> ")
            flap_times = options7(new_choice_input, flap_times)       # FUNC OPTION 7
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")

def options3(choice_input):
    print("")
    if choice_input.upper() == 'REFUSE':
        print("You stay in home and try to make some exercises, but when you try to extends in the floor, you get's tired again and fall asleep...")
        new_choice_input = 'sleep'
        options1(new_choice_input)       # FUNC OPTION 1
    elif choice_input.upper() == 'GET READY':
        print("You get ready to climb the hill, then you write him to confirm. When you are about to get out, you think in what vehicle carry.")
        while True:
            new_choice_input = input("How do you want to go? on FOOT, BIKE or STILTS?\n> ")
            options5(new_choice_input)       # FUNC OPTION 5
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")

def options4(choice_input):
    print("")
    if choice_input.upper() == 'RUN':
        print("You leave your apartment and run down the hall, while the neighbors try to get out and keep to stay up.")
        while True:
            new_choice_input = input("What do you want to take, ELEVATOR or STAIRS?\n> ")
            options6(new_choice_input)       # FUNC OPTION 6
    elif choice_input.upper() == 'HIDE':
        print("You quicly hide under the bed, and seconds before the build stops to shake it, you still stay there, seconds before you hear some sounds coming from below and put your ear in the floor to hear it better, suddenly feel how the the entire structure of the building gives way and falls to the earth. You feel how your cheest is pressed to the floor an suddenly you are floating and...")
        input("\n(Press enter to continue)\n")
        firstChoice(False)       # START AGAIN
    elif choice_input.upper() == 'KEEP CALM':
        print("You try to keep calm and wait for it to stop, which happens seconds later but with a violent jolt and the horrible crackle of the columns, you feel the entire building tilt and everything starts to slide. You try to hold on to the counter but you let go and fall through the broken windows.")
        flap_times = 0
        while True:
            new_choice_input = input("You want to FLAP your arms or just CLOSE your eyes.? \n> ")
            flap_times = options7(new_choice_input, flap_times)       # FUNC OPTION 7
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")

def options5(choice_input):
    print("")
    if choice_input.upper() == 'FOOT':
        print("You tell your friend and he come for you, then you go to the hill and a couple hours after reach the top. The views are awesome! The sun rises from the horizon... it's a wonder. You stay there a hald hour and when your about to go down, a horrible crackle stop you, then the earth violent shakes and seconds before, it stops. You hear your friend scream to look the city and at the distance you saw how the buildings fall, but suddenly the hill begans to crumble, and although you try to keep the balance the earth under your feets carry you to the abyss.")
        flap_times = 0
        while True:
            new_choice_input = input("You want to FLAP your arms or just CLOSE your eyes.? \n> ")
            flap_times = options7(new_choice_input, flap_times)       # FUNC OPTION 7
    elif choice_input.upper() == 'BIKE':
        print("You tell your friend and both quickly reach the top rinding your bikes. After witness the sunrise, taking some photos and some stunts, you trace the route to go down. So you drop down the hill but feel really unsteady, finding the first field to stop you wait for your friend but again feels like the world is moving, you think you're dizzy but suddenly your friends appear and scream you \"it's shaking\". It's very dangerous stay there so you continue going down and seconds before you hear a noise behind you, then you see the hill crumble and big rocks falling from the rock walls. You and your friend speed up, but another crackle fills the air and then the entire hill explodes and you sends flying with the bike and a piece of earth under you. Then you feel how are you falling and...")
        input("\n(Press enter to continue)\n")
        firstChoice(False)       # START AGAIN
    elif choice_input.upper() == 'STILTS':
        print("Stilts...? Are you...? Ok, you're the boss. You go with your friend and began to climb on stilts, and how the bad idea it is, while you was trying to dangerously keep balance, you stumble and fall to the abyss... what was you waiting for...?")
        flap_times = 0
        while True:
            new_choice_input = input("You want to FLAP your arms or just CLOSE your eyes.? \n> ")
            flap_times = options7(new_choice_input, flap_times)       # FUNC OPTION 7
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")

def options6(choice_input):
    print("")
    if choice_input.upper() == 'ELEVATOR':
        print("The door is close, but help of the neighbor you open the door, you jump inside but you hear the noise of metal cables snapping and the elevator shakes, and seconds later you fall into complete darkness")
        input("\n(Press enter to continue)\n")
        firstChoice(False)       # START AGAIN
    elif choice_input.upper() == 'STAIRS':
        print("The stairs shake and the raillings brakes, a violent shake trows you to the bottom of the dark pit...")
        input("\n(Press enter to continue)\n")
        firstChoice(False)       # START AGAIN
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")


def options7(choice_input, flap_times):
    print("")
    if choice_input.upper() == 'FLAP':
        if flap_times == 0:
            print("Seriosly? Your not a birth")
            flap_times = flap_times + 1
        elif flap_times >= 1:
            print("Nothing happen... your not a bird...")
            flap_times = flap_times + 1
        if flap_times == 3:
            print("Well maybe if you still trying something could happen.")
            flap_times = flap_times + 1
        if flap_times == 10:
            print("Nah, nothing happen, sorry...")
            flap_times = flap_times + 1
        if flap_times >= 20 and flap_times < 30:
            print("I suggest try to CLOSE your eyes.")
            flap_times = flap_times + 1
        elif flap_times >= 30:
            print("I strongly suggest try to CLOSE your eyes.")
    elif choice_input.upper() == 'CLOSE':
        print("It's the better option but the fall sense is pressed your chess, then you open the eyes again and see how the floor is getting close so quicly, until...")
        input("\n(Press enter to continue)\n")
        firstChoice(False)       # START AGAIN
    else:
        print(f"There is no option for the action: {choice_input}. \nTry again typing one of the options.\n")
        input("loading...       (Press enter to continue)\n")
    return flap_times

if __name__ == '__main__':
    print("-------- HISTORY GAME --------")
    firstChoice(True)