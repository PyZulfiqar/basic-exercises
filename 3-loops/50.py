import os

def get_natural():

    try:
        foo = int(input("\x1b[1m\x1b[32mEnter a natural number: \x1b[0m"))
        if foo < 1:
            print("\x1b[1m\x1b[31mNot a natural number!, Try again.\x1b[0m")
            return get_natural()
        else:
            return foo
    except ValueError:
        print("\x1b[1m\x1b[31mInvalid input, Try again.\x1b[0m")
        return get_natural()

def get_float():

    try:
        foo = float(input("\x1b[1m\x1b[32mEnter a float number: \x1b[0m"))
        return foo
    except ValueError:
        print("\x1b[1m\x1b[31mInvalid input, Try again.\x1b[0m")
        return get_natural()


def main():

    if os.system == 'nt':
        os.system('') 
    

    os.system('cls' if os.name == 'nt' else 'clear')

    natural = get_natural() 

    decimal = get_float()

    foo = 1
    for i in range(natural):
        foo *= decimal

    print(f"\x1b[1m\x1b[32m{foo}\x1b[0m")



if __name__ == "__main__":
    main()