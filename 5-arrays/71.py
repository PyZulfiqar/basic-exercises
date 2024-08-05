ansii = {
    "green": "\x1b[32m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

def convert_base(x, b):


    tmp = "" 
    arr: list[int] = [0]
    index = 0
    while True:
        r = x % b
        x = x // b
        if x < b:
            foo = [None for i in range(len(arr) + 1)]
            for i in range(len(arr)):
                foo[i] = arr[i]
            arr = foo[:]

            arr[index] = r
            arr[index + 1] = x
            break

        else:
            arr[index] = r
            foo = [None for i in range(len(arr) + 1)]
            for i in range(len(arr)):
                foo[i] = arr[i]
            index += 1 
            arr = foo[:]


    return arr 

def get_number(v):

    while True:
        try:
            n = int(input(f"{ansii['green']}Enter {v}: {ansii['reset']}")) 
            if n < 1:
                print(f"{ansii['red']}Invalid number, Try again.{ansii['reset']}")
            else:
                if v == 'x':
                    return n
                else:
                    if n >= 10 or n == 1:
                        print(f"{ansii['red']}Invalid number, Try again.{ansii['reset']}")
                    else:
                        return n
        except ValueError:
                print(f"{ansii['red']}Invalid input, Try again.{ansii['reset']}")
                return get_number(v)

def main():
    
    x = get_number('x')
    #b = get_number('b')
    foo =convert_base(x, 2)

    print(f"{ansii['green']}{x} in base 2 is: ", end='')
    for i in range(len(foo) - 1, -1, -1):
        print(foo[i], end='')
    print(f"{ansii['reset']}")

if __name__ == "__main__":
    main()