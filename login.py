import re
emailReg = r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
specChar = r'[.!@#$%^&*()\-=_+/?<>`~\[\]]'
capLetter = r'[A-Z]'
lengthReq = r'.{12,}'


def login(email, password):
    # check if user id and password are in users file
    users = open(r"users.txt")
    user = users.readline()
    while user != "":
        info = user.split(',')
        if info[0] == email:
            if info[1][:-1] == password:
                return True
            else:
                return False
        else:
            user = users.readline()
    users.close()
    return False


def register(email, password):
    # check if email is valid
    if not re.fullmatch(emailReg, email):
        return False

    # check if password is valid - capital letter, special character, 12+ length
    if not re.search(specChar, password) or not re.search(capLetter, password) or not re.search(lengthReq, password):
        return False

    # check if email already taken
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split(',')
        if info[0] == email:
            return False
        else:
            user = users.readline()
    users.close()

    # if it doesn't already exist, add to file
    users = open("users.txt", "a")
    users.write(email + "," + password + "\n")
    users.close()
    return True
