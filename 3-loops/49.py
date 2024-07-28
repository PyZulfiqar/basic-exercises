import os

def get_number():
    try:
        foo = float(input("\033[92m\x1b[1mEnter a number between -1 and +1:\x1b[0m "))
        if 0 <= abs(foo) < 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return foo
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\x1b[31m\x1b[1mInvalid number, Try again")
            return get_number()
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\x1b[31m\x1b[1mInvalid input, Try again")
        return get_number()

def main():

    # enable ansii escape characters for windows
    if os.name == 'nt':
        os.system('') 
    
    os.system('cls' if os.name == 'nt' else 'clear')

    c = 0
    sum_pos = 0
    while True:
        number = get_number()
        if number < 0:
            break
        else:
            sum_pos += number
            c += 1   
    
    avg = sum_pos / c if c > 0 else 'No positive numbers' 

    print(f"\033[92m\x1b[1mThe average of the positive numbers: \x1b[30m\x1b[47m{avg}\x1b[0m")

if __name__ == "__main__":
    main()