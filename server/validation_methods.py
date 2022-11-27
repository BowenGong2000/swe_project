
def Username_Validation(Username):
    if len(Username) > 5:
        return True
    return False


def Phone_Validation(Phone):
    if isinstance(int(Phone), int) and len(str(Phone)) == 10:
        return True
    return False


def Password_Validation(Password):
    if len(Password) > 8:
        return True
    return False


def Postlength_Validataion(Postinfo):
    if len(Postinfo) < 500:
        return True
    return False


def User_Validation(User):
    ret = Password_Validation(User["password"])
    ret = ret and Username_Validation(User["name"])
    return ret and Phone_Validation(User["phone"])


def User_type(User):
    ret = User["type"]
    return ret


def Setting_type(User):
    setting = User["setting"]
    color = setting["color"]
    subscription = setting['subscription']
    return color, subscription


def account_validation(email, password):
    # todo check validation with data base
    # 1 user, 2 manager, 0 invalid
    # todo data base validatin
    return 1


def manager_info(email):
    # todo return manager info from db to view
    infos = {}
    infos['account']=""
    infos['application_title'] = ""
    infos['application_content'] = ""
    infos['application_email'] = ""
    infos['application_major'] = ""
    infos['application_school'] = ""
    return infos
