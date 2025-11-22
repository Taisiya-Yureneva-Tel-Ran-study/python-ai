def pythonicNameRe()->str:
    return r"[A-Za-z_]\w*"

def passwordRe():
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z#$%\d_-]{8,}"

def ipV4AddressRe()->str:
    return r"((25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|\d{2}|\d{1})\.){3}(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|\d{2}|\d{1}){1}"

def mobileIsraelNumberRe()->str:
    return r"(\+972|0)(-*)(5[0-9])(-*)(\d(-*)(\d{2}(-*)){2}\d{2})"
