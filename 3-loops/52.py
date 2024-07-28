import os

ansii = {
    "green": "\x1b[32m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

def reverse_n(n):

    foo = 0
    while(n >= 1):
        r = n % 10
        foo = (foo * 10) + r
        n = n // 10
    return foo

def get_natural():

    try:
        n = int(input(f"{ansii['green']} Enter a natural number: {ansii['reset']}"))
        if n < 1:
            print(f"{ansii['red']} Not a natural number, Try again. {ansii['reset']}")
            return get_natural()
        else:
            return n
    except ValueError:
        print(f"{ansii['red']} Invalid input, Try again. {ansii['reset']}")
        return get_natural()

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    natural = get_natural()

    os.system('cls' if os.name == 'nt' else 'clear')

    r_natural = reverse_n(natural)
 
    mult = natural * r_natural

    print(f"{ansii['blue']}{ansii['white_bg']}{'Number':^13}{'Rversed':^13}{'Multiplication':^13}{ansii['reset']}")

    print(f"\x1b[1m{natural:^13}{r_natural:^13}{mult:^13}{ansii['reset']}")
if __name__ == "__main__":
    main()