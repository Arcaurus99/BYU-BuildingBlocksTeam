def letterGradeCalculator(value_grade):

    letter = ''

    if value_grade >= 90:
        letter = 'A'
    elif value_grade >= 80:
        letter = 'B'
    elif value_grade >= 70:
        letter = 'C'
    elif value_grade >= 60:
        letter = 'D'
    else:                       # elif value_grade < 60:
        letter = 'F'
    return letter

def calification(letter, value_grade):
    value = value_grade
    message = ''
    if value_grade > 70:
        message = "Good job!"
    else:
        message = "Good try! Just keep trying"

    sign = signCalc(value_grade)
    letter += sign

    print(f"Letter grade: \t\t {letter}\n"
        f"Percentage value: \t {value}\n"
        + message)
    
def signCalc(value_grade):
    sign = ''
    if value_grade >= 60 and value_grade <= 92:
        unitDigit = value_grade % 10
        if unitDigit >= 7 and unitDigit <= 9:
            sign = '+'
        if unitDigit >= 0 and unitDigit <= 2:
            sign = '-'
    return sign


if __name__ == '__main__':

    while True:
        print("\n------ LETTER GRADE CALCULATOR ------")

        value_grade = int(input("Insert grade value (percentage): "))
        letter_grade = letterGradeCalculator(value_grade)
        calification(letter_grade, value_grade)

        print("-------------------------------------")