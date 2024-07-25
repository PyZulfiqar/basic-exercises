# isn't 1 the lowest common divisor for all integers except 0?!
def get_number(value):

    try:
        return int(input(f"Please enter {value} Integer: "))
    except ValueError:
        print("That's not an integer, Try again!")
        return get_number(value)


def find_lcm(a, b):

    # a is considered smaller than be in the function
    i = a
    while(i % b != 0):
        i = i + a
    return i


def main():

    x = get_number("first")
    y = get_number("second")

    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1

    if x <= y:
        lcm = find_lcm(x, y)
    else:
        lcm = find_lcm(y, x)
    
    print(lcm)

if __name__ == "__main__":
    main()