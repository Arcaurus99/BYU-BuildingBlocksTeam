
print("Please enter the following:")
print()

# Declare article global variable
var_article = ''

# TESTING VALUES (comment this before send)
"""
var_adjective = 'happy'
var_animal = 'zebra'
var_verb1 = 'sneeze'
var_exclamation = 'hooray'
var_verb2 = 'read'
var_verb3 = 'drive'
var_noun = 'chair'
var_verb4 = 'dance'
print(f"adjective: {var_adjective}")
print(f"animal: {var_animal}")
print(f"verb: {var_verb1}")
print(f"exclamation: {var_exclamation}")
print(f"verb: {var_verb2}")
print(f"verb: {var_verb3}")
print(f"noun: {var_noun}")
print(f"verb: {var_verb4}")
"""

# INPUT ASSIGNMENT (uncomment this before send)
var_adjective = input("adjetive: ")
var_animal = input("animal: ")
var_verb1 = input("verb: ")
var_exclamation = input("exclamation: ")
var_verb2 = input("verb: ")
var_verb3 = input("verb: ")
var_noun = input("noun: ")
var_verb4 = input("verb: ")

# AN OR A FUNCTION
#print('\n' + var_noun[0])
vowels = ('a', 'e', 'i', 'o', 'u')
if var_noun != '':
    for v in vowels:
        if (var_noun[0] == v):
            var_article = 'an'
            break
        else:
            var_article = 'a'
else:
    var_article = 'a'   # To simplify, if no value is given to be compared, the article will be 'a' by default
#print(var_article)

# FORMAT
print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very\n"
    f"{var_adjective.lower()} {var_animal.lower()} {var_verb1.lower()} down the hallway. \"{var_exclamation.capitalize()}!\" I yelled. But all\n"
    f"I could think to do was to {var_verb2.lower()} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {var_verb3.lower()}\n"
    f"right in front of my family.\n"
    f"Then {var_article} {var_noun.lower()} fell down the stairs into my hands,\n"
    f"and it scared me so much that i started to {var_verb4.lower()}\n"
    f"until I fell out the bed and woke up\n")
