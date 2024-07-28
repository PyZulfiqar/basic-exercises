import os

ansii = {
    "green": "\x1b[32m",
    "red": "\x1b[31m",
    "bold": "\x1b[1m",
    "blue": "\x1b[34m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m"
}

def sum_digits(n):

    foo = 0
    while (n >= 1):
        foo += n % 10
        n = n // 10
    return foo

def check_divisble(a, b):

    if a % b == 0:
        return True
    else:
        return False

def print_divisble(n, d):

    return f"{ansii['bold']}{ansii['underline']}{n:^10}{d:^10}{n // d:^10}{ansii['reset']}"

def main():

    if os.name == 'nt':
        os.sysem('')
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{ansii['blue']}{ansii['white_bg']}{ansii['bold']}{'Number':^10}{'Sum':^10}{'Result':^10}{ansii['reset']}")

    for i in range(10, 101):

        foo = sum_digits(i)
        if check_divisble(i, foo):
            print(print_divisble(i, foo))

if __name__ == "__main__":
    main()