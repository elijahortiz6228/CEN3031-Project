def login(userID, password):
    # check if user id and password are in users file
    users = open(r"users.txt")
    user = users.readline()
    while user != "":
        info = user.split(',')
        if info[0] == userID:
            if info[1][:-1] == password:
                return userID
            else:
                return "Incorrect password"
        else:
            user = users.readline()
    users.close()
    return "User does not exist"


def register(userID, password):
    # need to add functionality to check if username or password is a valid one

    # check if username already exists
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split(',')
        if info[0] == userID:
            return "username already taken"
        else:
            user = users.readline()
    users.close()
    # if it doesn't already exist, add to file
    users = open("users.txt", "a")
    users.write(userID + "," + password + "\n")
    users.close()
    return "new user created"



