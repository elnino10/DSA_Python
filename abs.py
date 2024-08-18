"""abs module"""

def abs(n):
    """returns absolute value of given number"""
    if not isinstance(n, int):
        return "value is not a number"
    
    if n < 0:
        return n * -1
    return n


print(abs(-29))
print(abs('54'))
print(abs('a'))
print(abs(4))
print(abs(59))