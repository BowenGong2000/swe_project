import re

def Email_Validation(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.match(pat, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def Username_Validation(Username):
    if(len(Username) > 5):
        return True
    return False

def Phone_Validation(Phone):
    if isinstance(Phone, int) and len(str(Phone)) == 9:
        return True
    return False

def Password_Validation(Password):
    if len(Password) > 8:
        return True
    return False