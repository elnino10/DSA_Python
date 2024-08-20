"""print_to_98.py"""


def print_to_98(n):
    """prints from n to 98"""
    for i in range(n, 99):
        if i != 98:
            print(f"{i}, ", end="")
        else:
            print(f"{i}")


print_to_98(98)
print_to_98(50)
print_to_98(90)
print_to_98(0)