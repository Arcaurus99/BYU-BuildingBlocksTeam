# GIT HUB CHROMA KEY PROJECT
# https://github.com/RaulSanchezVazquez/chroma-key-composition

from PIL import Image

def chromaKey():
    x = 0
    y = 0
    for x in range(0, width_chroma):
        for y in range(0, height_chroma):
            (r_fore, g_fore, b_fore) = pixels_chroma[x, y]
            # print(f'{r_fore}, {g_fore}, {b_fore}')
            green_value = (r_fore + b_fore) - g_fore
            
            if green_value < -30:
                # print(green_value)
                pixels_chroma[x, y] = pixels_back[x, y]

img_foreground.show()



# SAVE IMAGE
def saveImage():
    while True:
        var_if_again = input("\nImage converted.\nDo you want to save it? (yes/no) ")
        if var_if_again.lower() == 'yes':
            name_new_image = input('Insert name of the new image (Whitout the extension).\n- ')
            img_extension = name_new_image + '.jpg'
            path_new_image = 'W07 Images/tests/' + img_extension
            print(f'Saved as:\t{img_extension} \nLocation:\tD:/arc/UNIVERSIDAD/BYU/Third Trimester/BYU-BuildingBlocksTeam/{path_new_image}\n')
            img_foreground.save(path_new_image)
            break
        elif var_if_again.lower() == 'no':
            print('Bye!\n')
            break
        else:
            print("I don't understand. Try again! \n")

if __name__ == '__main__':
    
    # - BACKGROUND IMAGE PATH
    img_background = Image.open('W07 Images/star_wars/bg.png')
    # - FOREGROUND IMAGE PATH
    img_foreground = Image.open('W07 Images/star_wars/fighter.jpg')

    width_chroma, height_chroma = img_foreground.size
    width_back, height_back = img_foreground.size

    pixels_chroma = img_foreground.load()
    pixels_back = img_background.load()

    chromaKey()

    # saveImage()