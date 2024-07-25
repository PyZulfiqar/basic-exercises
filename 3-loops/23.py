def get_number(value):

    try:
        return int(input(f"Please enter {value} Integer: "))
    except ValueError:
        print("That's not an integer, Try again!")
        return get_number(value)


def find_cd(a, b):

    # a is considered smaller than be in the function
    print("Common Divisors: ", end='')
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            print(i, end=' ')
    print()


def main():

    x = get_number("first")
    y = get_number("second")

    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1


    if x <= y:
        find_cd(x, y)
    else:
        find_cd(y, x)

if __name__ == "__main__":
    main()