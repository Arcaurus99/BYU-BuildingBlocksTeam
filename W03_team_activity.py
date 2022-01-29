from math import pi

#ALL
def all():
    coreRequirements()
    stretchChallenge()

#---------- CORE REQUIREMENTS ----------
def coreRequirements():
    print("---- CORE REQUIREMENTS ----\n")
    coreSquare()
    coreRectangle()
    coreCircle()

def coreSquare():
    var_sq_len = float(input("What is the length of a side of the square? "))
    print(f"R/ The area of the square is: {var_sq_len ** 2}\n")

def coreRectangle():
    var_rc_len = float(input("What is the length of rectangle? "))
    var_rc_wid = float(input("What is the width of the rectangle? "))
    print(f"R/ The area of the rectangle is: {var_rc_len * var_rc_wid}\n")

def coreCircle():
    var_cir_rad = float(input("What is the radius of the circle? "))
    print(f"R/ The area of the circle is: {pi * (var_cir_rad ** 2)}\n")

#---------- STRETCH CHALLENGE ----------
def stretchChallenge():
    print("---- STRETCH CHALLENGE ----\n")
    challenge01()
    challenge02()
    challenge03Square()
    challenge03Rectangle()
    challenge03Circle()

def challenge01():
    print(f"The imported value of Pi is: {pi}\n")

def challenge02():
    var_len = float(input("Insert a length value: "))
    print(f"Square/ The area of a square with a length of {var_len} is: {var_len ** 2}"
        f"\nCircle/ The area of the circle with a radius of {var_len} is: {pi * (var_len ** 2)}"
        f"\nCube/ The volume of a cube with a length of {var_len} is: {var_len ** 3}"
        f"\nSphere/ The volume of the sphere with a radius of {var_len} is: {(4/3) * pi * (var_len ** 3)}\n")

def challenge03():
    challenge03Square()
    challenge03Rectangle()
    challenge03Circle()

def challenge03Square():
    var_sq_len = float(input("What is the length of a side of the square in centimeters? "))
    var_sq_area = var_sq_len ** 2           # The area was calculated in centimeters
    print(f"R/ The area of the square with a length of {var_sq_len}cm is:\n"
        f"{var_sq_area}cm^2 (centimeters) or {var_sq_area / 10000}m^2 (meters)\n")

def challenge03Rectangle():
    var_rc_len = float(input("What is the length of rectangle in centimeters? "))
    var_rc_wid = float(input("What is the width of the rectangle in centimeters? "))
    var_rc_area = var_rc_len * var_rc_wid            # The area was calculated in centimeters
    print(f"R/ The area of the rectangle a length of {var_rc_len}cm and a with of {var_rc_wid}cm is:\n"
        f"{var_rc_area}cm^2 (centimeters) or {var_rc_area / 10000}m^2 (meters)\n")

def challenge03Circle():
    var_cir_rad = float(input("What is the radius of the circle in centimeters? "))
    var_cir_area = {pi * (var_cir_rad ** 2)}            # The area was calculated in centimeters
    print(f"R/ The area of the circle with radius of {var_cir_rad}cm is:\n"
        f"{var_cir_area}cm^2 (centimeters) or {var_cir_area / 10000}m^2 (meters)\n")

if __name__ == '__main__':
    challenge03()

