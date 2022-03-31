from math import pi

def areaSquare(side):
    area = side ** 2
    return area

def areaRectangle(length, width):
    area = length * width
    return area

def areaCircle(rad):
    area = pi * (rad ** 2)
    return area

if __name__ == '__main__':

    while True:
        shape = input('\nWhat kind of shape do you have?\n(Square, Rectangle or Circle. Write Quit to finish)\n- ')
        
        if shape.lower() == 'square':
            print('-- SQUARE --')
            value_side = int(input("What is the length of a side of the square? "))
            value_area = areaSquare(value_side)
            print(f'The value of your area is {value_area}') 

        elif shape.lower() == 'rectangle':
            print('-- RECTANGLE --')
            value_length = int(input("What is the length of rectangle? "))
            value_width = int(input("What is the width of rectangle? "))
            value_area = areaRectangle(value_length, value_width)
            print(f'The value of your area is {value_area}') 

        elif shape.lower() == 'circle':
            print('-- CIRCLE --')
            value_rad = int(input("What is the radius of the circle? "))
            value_area = areaCircle(value_rad)
            print(f'The value of your area is {value_area:.2f}') 

        elif shape.lower() == 'quit':
            break

        else:
            print(f'{shape} is not a valid option. Try again')

"""
def areaSquare():
    var_sq_len = float(input("What is the length of a side of the square? "))
    print(f"R/ The area of the square is: {var_sq_len ** 2}\n")

def areaRectangle():
    var_rc_len = float(input("What is the length of rectangle? "))
    var_rc_wid = float(input("What is the width of the rectangle? "))
    print(f"R/ The area of the rectangle is: {var_rc_len * var_rc_wid}\n")

def areaCircle():
    var_cir_rad = float(input("What is the radius of the circle? "))
    print(f"R/ The area of the circle is: {pi * (var_cir_rad ** 2)}\n")
"""