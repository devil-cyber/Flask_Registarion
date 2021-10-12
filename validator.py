import re


def CheckPassword(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"

    # compiling regex
    pattern = re.compile(reg)

    # searching regex
    res = re.search(pattern, password)

    # validating conditions
    if res:
        return True
    else:
        return False


def CheckEmail(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        return True
    else:
        return False
