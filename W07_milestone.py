# STEPS
# https://byui-cse.github.io/cse110-course/lesson07/prove.html
# CHROMA KEY TECHNIQUE (Visual Effect)
# https://en.wikipedia.org/wiki/Chroma_key
# GIT HUB CHROMA KEY PROJECT
# https://github.com/RaulSanchezVazquez/chroma-key-composition

from PIL import Image

# - BACKGROUND IMAGE PATH
img_background = Image.open('W07 Images/sunset.jpg')
# - FOREGROUND IMAGE PATH
img_foreground = Image.open('W07 Images/boat.jpg')

width, height = img_foreground.size

pixels_chroma = img_foreground.load()
pixels_back = img_background.load()

x = 0
y = 0
for x in range(0, width):
    for y in range(0, height):
        (r_fore, g_fore, b_fore) = pixels_chroma[x, y]
        # print(f'{r_fore}, {g_fore}, {b_fore}')
        green_value = (r_fore + b_fore) - g_fore
        
        if green_value < -30:
            # print(green_value)
            pixels_chroma[x, y] = pixels_back[x, y]

        if r_fore < 100 and g_fore > 122 and b_fore < 100:
            pixels_chroma[x, y] = pixels_back[x, y]
        elif r_fore < 160 and g_fore > 160 and b_fore < 160:
            pixels_chroma[x, y] = pixels_back[x, y]

img_foreground.show()

# SAVE IMAGE
# while True:
#     var_if_again = input("\nImage converted.\nDo you want to save it? (yes/no) ")
#     if var_if_again.lower() == 'yes':
#         name_new_image = input('Insert name of the new image (Whitout the extension).\n- ')
#         img_extension = name_new_image + '.jpg'
#         path_new_image = 'W07 Images/tests/' + img_extension
#         print(f'Saved as:\t{img_extension} \nLocation:\tD:/arc/UNIVERSIDAD/BYU/Third Trimester/BYU-BuildingBlocksTeam/{path_new_image}\n')
#         img_foreground.save(path_new_image)
#         break
#     elif var_if_again.lower() == 'no':
#         print('Bye!\n')
#         break
#     else:
#         print("I don't understand. Try again! \n")
    
"""#//////// DOC //////////

# - OPEN IMAGE
# <<image_name>> = Image.open("<<path>>")
image_original = Image.open("W07 Images/beach.jpg")

# - DISPLAY in default app
# <<image_name>>.show()
image_original.show()

# - SIZE
# <<var_width>>, <<var_height>> = <<image_name>>.size
width, height = image_original.size

# - PIXELS ACCESS
# <<var_pixels>> = <<image_name>>.load()
pixels_original = image_original.load()

# - GET RGB VALUES (x and y are the coodinates values)
# <<var_r>>, <<var_g>>, <<var_b>> = <<var_pixels>>[x, y]
r, g, b = pixels_original[100, 200]

# - SET RGB VALUES (r, g and b reffer to respective values: red, green and blue)
# <<var_pixels>>[x, y] = (r, g, b)
pixels_original[100, 200] = (50, 60, 70)

# - SAVE (New Image)
# <<image_name>>.save("<<name>>.<<extension>>")
image_original.save("the_file_goes_here.jpg")

# - CREATE (New Image)
# <<image_name_2>> = Image.new("RGB", <<image_name_1>>.size)
image_new = Image.new("RGB", image_original.size)"""
