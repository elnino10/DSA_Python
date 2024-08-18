"""is-Alpha module"""

def isAlpha(c):
    """function checks if arg is alphabet"""
    if isinstance(c, str) and len(c) == 1:
        if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90):
            return 1
    return 0


print(isAlpha('50'))
print(isAlpha('d'))
print(isAlpha('A'))
print(isAlpha('3'))
print(isAlpha(8))