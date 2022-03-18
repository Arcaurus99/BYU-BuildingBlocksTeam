
print()
with open('./hr_system.txt') as data_list:
    for data in data_list:
        name, id_number, job_title, salary = data.split(' ')
        salary = float(salary)/24   # twice(2) month(12) in year = 24
        if job_title == 'Engineer':
            salary += 1000
        print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}'.strip())
        # Alexia (ID: 1913), Engineer - $4500.00
print()
