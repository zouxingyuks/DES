# PKCS5
def addPadding(s):
    p = 8 - len(s) % 8
    return s + p * chr(p).encode()


def delPadding(s):
    p = s[-1]
    return s[:-p]
