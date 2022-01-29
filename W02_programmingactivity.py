
print("Please enter the following information:")
print()

# TEST INFO
name = "Esteban"
last_name = "Arcos"
email = "estebanar@unicauca.edu.co"
phone = "(208) 555-1234"
job = "Student"
id = "83-23821"
hair_color = "Brown"
eye_color = "Brown"
month = "September"
training = "Yes"

# INPUT INFO
"""
name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job = input("Job title: ")
id = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")
"""

# FORMAT
print("\nThe ID Card is:")
print("--------------------------------------------")
print(f"{last_name.upper()}, {name.capitalize()}")
print(job.title())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair_color} \t\t Eyes: {eye_color}")
print(f"Month: {month} \t Training: {training}")
print("--------------------------------------------")