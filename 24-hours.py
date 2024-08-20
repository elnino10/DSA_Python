"""24-hours"""


def print_minutes():
    """prints every minute of the day"""
    for hour in range(24):
        for minute in range(60):
            print(f"{hour :02d}:{minute :02d}")


print_minutes()