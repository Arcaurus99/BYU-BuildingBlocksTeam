people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 100
youngest_name = ''

print('-- Data Person List --')

for person in people:
    name, age_str = person.split(" ")
    age = int(age_str)
    print(f'Age: {age} - Name: {name}')
    if youngest_age > age:
        youngest_age = age
        youngest_name = name

print(f'The youngest person name is {youngest_name}, and has {youngest_age} years old.')