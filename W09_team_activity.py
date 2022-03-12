
from audioop import avg


new_number = 1
num_list = []
num = 0

print("Enter a list of numbers, type 0 when you finish.")

while new_number != 0:
    new_number = int(input('Enter a number: '))
    num_list.append(new_number)

for num in num_list:
    sum = sum + num

print(f"Sum: {sum}")

print(f"Average: {sum / len(num_list)}")

print(f"Max: {max(num_list)}")

