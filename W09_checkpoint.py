
friendsList = []

def friendsListAdd():
    while True:
        name = input("Type the name of a friend: ")

        if name == 'end':
            break
        else:
            friendsList.append(name)

def showFriends():
    print("\nYour friends are: ")
    for friend in friendsList:
        print(friend)

if __name__ == '__main__':
    
    friendsListAdd()

    showFriends()