import re

emailReg = r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
specChar = r'[.!@#$%^&*()\-=_+/?<>`~\[\]]'
capLetter = r'[A-Z]'
lengthReq = r'.{12,}'
phoneNum = r'^\\+?[1-9][0-9]{7,14}$'


def emailValid(email):
    if not re.fullmatch(emailReg, email):
        return False
    else:
        return True

def passValid(password):
    if not re.search(specChar, password) or not re.search(capLetter, password) or not re.search(lengthReq, password):
        return False
    else:
        return True

def phoneValid(phoneNum):
    if not re.match(phoneNum, phoneNum):
        return False
    else:
        return True

def charity_register(name, email, password, phoneNumber, address, charityType, charityBio):
    name = name
    address = address
    charityType = charityType
    charityBio = charityBio

    if not emailValid(email):
        return False

    if not passValid(password):
        return False

    if not phoneValid(phoneNumber):
        return False

    charities = open("charities.txt", "r")
    charity = charities.readline()
    while charity != "":
        info = charity.split(',')
        if info[1] == email:
            return False
        else:
            charity = charities.readline()
    charities.close()

    charities = open("charities.txt", "a")
    charities.write(name + "," + email + "," + password + "," + phoneNumber + "," + address + "," + charityType + "," + charityBio + "\n")
    charities.close()
    return True


def charity_search(name):
    charities = open("charities.txt", "r")
    charity = charities.readline()
    while charity != "":
        info = charity.split(',')
        if info[0] == name:
            return True
        else:
            charity = charities.readline()
    charities.close()
