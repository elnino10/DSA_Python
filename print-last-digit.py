"""print-last-digit"""

def print_last_digit(n):
    """prints last digit of a given number"""
    if isinstance(n, int):
        print(n % 10, end="")
        return n % 10
    return "invalid input"


print_last_digit(246)
print_last_digit(3)
num = print_last_digit(90)
print(num)
print_last_digit(24)