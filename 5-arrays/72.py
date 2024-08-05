import os

ansii = {
    "green": "\x1b[32m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

def num_to_arr(n):

    arr: list[int] = [0]
    indx = 0
    foo: list[int] = [0]
    while(n >= 1):
        r = n % 10
        arr[indx] = r
        n = n // 10
        if n < 1:
            foo = [None for i in range(len(arr))]
        else:
            foo = [None for i in range(len(arr) + 1)]
        for i in range(len(arr)):
            foo[i] = arr[i]
        indx += 1
        arr = foo[:]
    return arr 

def reverse_arr(arr):


    tmp = [None for i in range(len(arr))]

    foo = len(arr) - 1
    bar = len(arr) - 1
    for i in range(len(arr) -1, -1, -1):
        tmp[foo - bar] = arr[i]
        bar -= 1
    
    return tmp

        

def get_natural():

    while True:
        try:
            n = int(input(f"{ansii['green']} Enter a natural number: {ansii['reset']}"))
            if n < 1:
                print(f"{ansii['red']} Not a natural number, Try again. {ansii['reset']}")
            else:
                return n
        except ValueError:
            print(f"{ansii['red']} Invalid input, Try again. {ansii['reset']}")

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    natural = get_natural()

    os.system('cls' if os.name == 'nt' else 'clear')

    
    foo = num_to_arr(natural)
    r_natural = reverse_arr(foo)

    check = 0

    for i in range(len(r_natural) - 1):
        if r_natural[i] == foo[i]:
            check += 1


    print(f"{ansii['blue']}{ansii['white_bg']}{'Number':^13}{'Palindromic':^13}{ansii['reset']}")

    if check == len(r_natural) - 1:
        print(f"\x1b[1m{natural:^13}{'yes':^13}{ansii['reset']}")
    else:

        print(f"\x1b[1m{natural:^13}{'No':^13}{ansii['reset']}")
if __name__ == "__main__":
    main()