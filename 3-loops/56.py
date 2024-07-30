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
    while True:
        r = x % b
        x = x // b
        if x < b:
            tmp = str(r) + tmp
            tmp = str(x) + tmp
            break
        else:
            tmp = str(r) + tmp
    
    return tmp

def get_number(v):

    try:
        n = int(input(f"{ansii['green']}Enter {v}: {ansii['reset']}")) 
        if n < 1:
            print(f"{ansii['red']}Invalid number, Try again.{ansii['reset']}")
            return get_number(v)
        else:
            if v == 'x':
                return n
            else:
                if n >= 10 or n == 1:
                    print(f"{ansii['red']}Invalid number, Try again.{ansii['reset']}")
                    return get_number(v)
                else:
                    return n
    except ValueError:
            print(f"{ansii['red']}Invalid input, Try again.{ansii['reset']}")
            return get_number(v)

def main():
    
    x = get_number('x')
    b = get_number('b')
    foo =convert_base(x, b)

    print(f"{ansii['green']}{x} in base {b} is: {foo}{ansii['reset']}")

if __name__ == "__main__":
    main()