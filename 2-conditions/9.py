def get_number(value):
    try:
        return float(input(f"Please Enter float number {value}: "))
    except ValueError:
        print("That's not a float number, Please try again!")
        return get_number(value)

def find_max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

def main():

    a = get_number(1)
    b = get_number(2)
    c = get_number(3)

    foo = find_max(a, b, c)

    print(f"Max is '{foo}'")

if __name__ == "__main__":
    main()