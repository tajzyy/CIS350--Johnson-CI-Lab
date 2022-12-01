def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def square_numbers(a, b):
    return a * a, b * b

def mod_numbers(a, b):
    return a % b


if __name__ == "__main__":
    print("Adding:", add_numbers(2,4))
    print("Subtracting:", subtract_numbers(9,2))
    print("Multiplying:", multiply_numbers(2,4))
    print("Dividing:", divide_numbers(9,2))
    print("Squaring:", square_numbers(2,4))
    print("Mod of:", mod_numbers(9,2))


