import os

ansii = {
    "green": '\x1b[32m\x1b[1m',
    "red": '\x1b[31m\x1b[1m',
    "blue": '\x1b[34m\x1b[1m',
    "white_bg": '\x1b[107m',
    "reset": '\x1b[0m',
    "underline": '\x1b[4m\x1b[1m'
}

def find_next(a, b):

    return (a + b) / 2

def solve(n):

    arr: list[int] = [None for i in range(n)]

    i = 2
    arr[0] = 1
    arr[1] = 5
    while(i < n):

        arr[i] = find_next(arr[i - 1], arr[i - 2])
        i += 1

    return arr[n - 1] 

def get_input():

    try:
        n = int(input(f"{ansii['green']}Enter a number to find the 'nth' term: {ansii['reset']}"))
        if n <= 0:
            print(f"{ansii['red']}Invalid number, Try again.{ansii['reset']}")
            return get_input()
        else:
            return n
    except ValueError:
        print(f"{ansii['red']}Invalid input, Try again.{ansii['reset']}")
        return get_input()
        
def main():

    if os.name == 'nt':
        os.system('')
    
    os.system('cls' if os.name == 'nt' else 'clear')


    n = get_input()

    if n == 1:
        print(f"\x1b[1mThe 1st term of the series: 1{ansii['reset']}")
    elif n == 2:
        print(f"\x1b[1mThe 2nd term of the series: 5{ansii['reset']}")
    elif n == 3:
        print(f"\x1b[1mThe 3rd term of the series: {solve(n)}{ansii['reset']}")
    else:
        print(f"\x1b[1mThe {n}th term in the series: {solve(n)}{ansii['reset']}")

if __name__ == "__main__":
    main()
