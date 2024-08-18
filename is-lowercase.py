"""is-lowercase"""

def is_lowercase(c):
    """function returns 1 if lowercase or 0 otherwise"""
    if isinstance(c, str) and len(c) == 1:
        if ord(c) >= 97 and ord(c) <= 122:
            return 1
    return 0
    


print(is_lowercase('98'))
print(is_lowercase('D'))
print(is_lowercase('s'))
print(is_lowercase('A'))