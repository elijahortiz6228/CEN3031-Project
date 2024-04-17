import re

emailReg = r'[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,7}'
specChar = r'[.!@#$%^&*()\-=_+/?<>`~\[\]]'
capLetter = r'[A-Z]'
lengthReq = r'.{12,}'


def emailValid(email):
    if not re.fullmatch(emailReg, email):
        return False
    return True


def passValid(password):
    if not re.search(specChar, password) or not re.search(capLetter, password) or not re.search(lengthReq, password):
        return False
    return True


def login(email, password):
    # check if user id and password are in users file
    users = open(r"users.txt")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            if info[1] == password:
                return True
            else:
                return False
        else:
            user = users.readline()
    users.close()


def register(email, password, security, first, last, state):
    # check if email is valid
    if not emailValid(email):
        return False

    # check if password is valid - capital letter, special character, 12+ length
    if not passValid(password):
        return False

    # check if email already taken
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            return False
        else:
            user = users.readline()
    users.close()

    # if it doesn't already exist, add to file
    users = open("users.txt", "a")
    users.write(email + "|" + password + "|" + security + "|" + first + "|" + last + "|" + state + "\n")
    users.close()
    return True


def forgotPasswordEmail(email):
    # just checks if the email exists
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            return True
        else:
            user = users.readline()
    users.close()
    return False


def forgotPassword(email, answer):
    # check that the email exists, and if it does, check if security question answer matches
    users = open("users.txt", "r")
    user = users.readline()
    while user != "":
        info = user.split('|')
        if info[0] == email:
            if info[2] == answer:
                return True
            return False
        else:
            user = users.readline()
    users.close()
    return False


def resetPassword(email, newPassword):
    # only use this if forgotPassword returns true
    userFile = open("users.txt", "r")
    users = userFile.read().split("\n")
    userFile.close()
    userFile = open("users.txt", "w")
    i = 0
    user = users[i]
    while user != "":
        i += 1
        info = user.split('|')
        if info[0] == email:
            userFile.write(
                info[0] + "|" + newPassword + "|" + info[2] + "|" + info[3] + "|" + info[4] + "|" + info[5] + "\n")
        else:
            userFile.write(user + "\n")
        user = users[i]
    userFile.close()

