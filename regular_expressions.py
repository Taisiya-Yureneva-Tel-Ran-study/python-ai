def pythonicNameRe()->str:
    return r"[A-Za-z_]\w*"

def passwordRe():
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z#$%\d_-]{8,}"

def getOctetRe()->str:
    return r"(25[0-5]|2[0-4][0-9]|[0-1]?\d{1,2})"

def ipV4AddressRe()->str:
    res = r"(" + getOctetRe() + r"\.){3}(" + getOctetRe() + r")"
    
    return res

def mobileIsraelNumberRe()->str:
    return r"(\+972|0)(-?)(5[0-9])(-?)(\d(-?)(\d{2}(-?)){2}\d{2})"
