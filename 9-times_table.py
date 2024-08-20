"""9-times_table"""

def times_table():
    """prints 9 times table starting from zero"""
    for i in range(10):
        for j in range(10):
            if j != 9:
                if j == 0:
                    print(f"{j * i}, ", end="")
                else:   
                    print(f"{j * i :2d}, ", end="")
            else:
                print(f"{j * i :3d}")


times_table()