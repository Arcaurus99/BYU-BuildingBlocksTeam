
value = int(input('How many columns and rows do you want in your multiplication table? ')) 

spaces = int(len(str(value * value)))

for x in range(value):
    x += 1
    # print(f'{x:3}', end = ', ')
    for y in range(value):
        y += 1
        print(f'{(y * x):{spaces}}' , end = ' ')
    print(end = '\n')

