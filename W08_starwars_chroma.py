# GIT HUB CHROMA KEY PROJECT
# https://github.com/RaulSanchezVazquez/chroma-key-composition

from hashlib import new
from PIL import Image

# CHROMA KEY
def chromaKey(img_background, img_foreground):
    img_new = Image.new("RGB", img_foreground.size)

    width_chroma, height_chroma = img_foreground.size

    pixels_chroma = img_foreground.load()
    pixels_back = img_background.load()

    x = 0 
    y = 0
    for x in range(0, width_chroma):
        for y in range(0, height_chroma):
            # print(pixels_chroma[x, y])
            try:
                (r_fore, g_fore, b_fore) = pixels_chroma[x, y]
            except:
                (r_fore, g_fore, b_fore, n) = pixels_chroma[x, y]
            # print(f'{r_fore}, {g_fore}, {b_fore}')
            green_value = (r_fore + b_fore) - g_fore

            if green_value < -30:
                pixels_chroma[x, y] = pixels_back[x, y]
            # elif r_fore < 100 and g_fore > 122 and b_fore < 100:
            #     pixels_chroma[x, y] = pixels_back[x, y]
            # elif r_fore < 160 and g_fore > 160 and b_fore < 160:
            #     pixels_chroma[x, y] = pixels_back[x, y]

    img_new = img_foreground

    return img_new

# SAVE IMAGE
def saveImage(img_save):
    while True:
        if_save = input("Yoda: \"The frame converted was. Save it do you want?\" (yes/no) ")
        if if_save.lower() == 'yes':
            name_new_image = input('Insert name of the new image (Whitout the extension).\n- ')
            img_extension = name_new_image + '.jpg'
            path_new_image = 'W07_Images/tests/' + img_extension
            print(f'Saved as:\t{img_extension}'
                f'\nLocation:\tD:/arc/UNIVERSIDAD/BYU/"Third Trimester"/BYU-BuildingBlocksTeam/{path_new_image}\n')
            img_save.save(path_new_image)
            break
        elif if_save.lower() == 'no':
            print('Bye!\n')
            break
        else:
            print("I don't understand. Try again! \n")

# MENU
def displayMenu():
    menu = ("Millennium Falcon",
            "X-wing",
            "R2-D2",
            "AT-ST",
            "Death Star",
            "TIE/LN")

    print("Yoda: \"Wisely should you choose, hmmm.\"\n"
        "--- Menu ---")
    for option in menu:
        print(option)
    print("------------")
    return input("Insert option name: ")


if __name__ == '__main__':
    
    # - BACKGROUND IMAGE PATH
    img_background = Image.open('W07_Images/star_wars/tatooine.jpg')
    # - FOREGROUND IMAGE PATH
    # Foreground image will be selected by user from menu

    print("\n------ STAR WARS CHROMA KEY ------\n"
        "Welcome to the world of STAR WARS!\n"
        "To start you are in the planet Tatooine.\n"
        "Select the option you want to set into \n"
        "the frame writing the name of it. \n"
        "The options abailable will be displayed.\n"
        "Yoda: \"May the Force be with you padawan!\"\n")
    input("(Press 'Enter' to continue.)\n")

    add_more = True

    while add_more:
        while True:
            selected_option = displayMenu().lower()

            if selected_option == 'millennium falcon':
                img_foreground = Image.open('W07_Images/star_wars/millennium_falcon.jpg')
                break
            elif selected_option == 'x-wing':
                img_foreground = Image.open('W07_Images/star_wars/x-wing.jpg')
                break
            elif selected_option == 'r2-d2':
                img_foreground = Image.open('W07_Images/star_wars/r2d2.jpg')
                break
            elif selected_option == 'at-st':
                img_foreground = Image.open('W07_Images/star_wars/atst.jpg')
                break
            elif selected_option == 'death star':
                img_foreground = Image.open('W07_Images/star_wars/death_star.jpg')
                break
            elif selected_option == 'tie/ln':
                img_foreground = Image.open('W07_Images/star_wars/tie.jpg')
                break
            else:
                input("\nYoda: \"Hmmmm, your selection, valid is not. Again try, you should.\"\n"
                    "(Press 'Enter' to continue.)\n")

        new_image = chromaKey(img_background, img_foreground)
        backup_image = new_image

        input("\nYoda: The frame ready is. To look it, 'Enter' press.")

        new_image.show()

        while True:
            if_add_more = input("\nDo you want to add more to the frame? (yes/no) ")
            print()
            if if_add_more.lower() == 'yes':
                img_background = new_image
                break
            elif if_add_more.lower() == 'no':
                add_more = False
                break
            else:
                print("I don't understand. Try again! \n")

    saveImage(new_image)