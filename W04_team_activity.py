import math

from W03_team_activity import challenge01

# fall speed in a fluid.
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
# v = sqrt((m*g)/c) * (1 - exp((-sqrt(m*g*c)/m)*t))

#---------- CORE REQUIREMENTS ----------
def coreRequirments():
    print("\n---------------------------------------------------------------\n"
        "Welcome to the velocity calculator. Please enter the following:\n")

    m = float(input("Mass (in kg): "))
    g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
    t = float(input("Time (in seconds): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    A = float(input("Cross sectional area (in m^2): "))
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    # Inner value
    c = (1 / 2) * p * A * C
    print(f"\nThe inner value of c is: {c:.3f}")

    # Speed value
    v = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
    print(f"The velocity after {t} seconds is: {v:.3f} m/s\n"
        "-------------------------------------------------")

#---------- STRETCH CHALLENGE ----------
def challenge01BowlingBall():
    print("\n---------------------------------------------------------------\n"
        "Welcome to the BOWLING BALL velocity calculator. Please enter the following:\n")

    m = 7.3
    print(f"Mass (in kg): {m}")
    g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
    t = float(input("Time (in seconds): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    r = float(input("Bowling ball radio (in cm, 10.8-11): "))
    A = math.pi * r ** 2
    print(f"Cross sectional area (in m^2): {A}")
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    # Inner value
    c = (1 / 2) * p * A * C
    print(f"\nThe inner value of c is: {c:.3f}")

    # Speed value
    v = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
    print(f"The velocity after {t} seconds is: {v:.3f} m/s\n"
        "-------------------------------------------------")

def challenge01Skydiver():
    print("\n---------------------------------------------------------------\n"
        "Welcome to the BOWLING BALL velocity calculator. Please enter the following:\n")

    m = 7.3
    print(f"Mass (in kg): {m}")
    g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
    t = float(input("Time (in seconds): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    r = float(input("Bowling ball radio (in cm, 10.8-11): "))
    A = math.pi * r ** 2
    print(f"Cross sectional area (in m^2): {A}")
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    # Inner value
    c = (1 / 2) * p * A * C
    print(f"\nThe inner value of c is: {c:.3f}")

    # Speed value
    v = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
    print(f"The velocity after {t} seconds is: {v:.3f} m/s\n"
        "-------------------------------------------------")

def challenge02():
    print("\n---------------------------------------------------------------\n"
        "Welcome to the velocity calculator. Please enter the following:\n")

    m = float(input("Mass (in kg): "))
    t = float(input("Time (in seconds): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    A = float(input("Cross sectional area (in m^2): "))
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    # Inner value
    c = (1 / 2) * p * A * C
    print(f"\nThe inner value of c is: {c:.3f}")

    # Speed value on Earth
    g = 9.8
    v_earth = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
    print(f"The velocity on EARTH (where gravity is 9.8 m/s^2) after {t} seconds is: {v_earth:.3f} m/s")

    # Speed value on Jupiter
    g = 24
    v_jupiter = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
    print(f"The velocity on JUPITER (where gravity is 24 m/s^2) after {t} seconds is: {v_jupiter:.3f} m/s\n\n"
        f"The difference of velocity after {t} seconds between Earth and Jupiter is {v_jupiter - v_earth}\n"
        "---------------------------------------------------------------")

def challenge03():
    print("\n---------------------------------------------------------------\n"
        "Welcome to the velocity calculator. Please enter the following:\n")

    m = float(input("Mass (in kg): "))
    g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
    p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
    A = float(input("Cross sectional area (in m^2): "))
    C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

    # Inner Value
    c = (1 / 2) * p * A * C
    print(f"\nThe inner value of c is: {c:.3f}")
    

    # Speed Value
    t = 1               # Tiempo (en segundos)
    var_times_v_repeated = 0
    t_terminal_computed = 0
    v_segundo_antes = 0
    print("-- CALCULATING THE SPEED EVERY ONE SECOND --")
    while True:
        # print(var_times_v_repeated)

        v = math.sqrt((m * g) / c) * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t ))
        print(f"The velocity after {t} seconds is: {v:.3f} m/s")
        
        v = float(f"{v:.3f}")
        if v == v_segundo_antes:
            t_terminal_computed = t         # Every time we found v repeat save the second
            var_times_v_repeated += 1       # Every time we found v repeat we increase the count 1
        else:
            var_times_v_repeated = 0        # If the values of v change, the count of times_v_repeat is reset
            v_segundo_antes = v             # Save the last value of v to compare in the next loop
        
        if var_times_v_repeated > 15:
            break                           # If the value of v repeat 16 times, the loop stops
        
        t += 1                          # The time increase 1 second
        
    
    # Terminal Velocity
    v_terminal = math.sqrt((m * g) / c)
    print(f"\nThe terminal velocity given by v_terminal = sqrt((m * g) / c) is: {v_terminal:.3f} m/s\n"
        f"The estimated terminal velocity was {v_segundo_antes:.3f} m/s and confirmed at {t_terminal_computed} seconds\n"
        "---------------------------------------------------------------\n")

if __name__ == "__main__":
    challenge03()