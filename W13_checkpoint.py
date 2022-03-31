def caseUpper(entry_msg):
    msg = entry_msg.upper()
    return msg

def caseLower(entry_msg):
    msg = entry_msg.lower()
    return msg

if __name__ == '__main__':
    entry = input('What is your message? ')
    print(entry)

    message = caseUpper(entry)
    print(message)

    message = caseLower(entry)
    print(message)