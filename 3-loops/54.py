def get_number(v):

    try:
        n = int(input(f"Please Enter {v} number: "))
        if n < 1:
            print("Invalid numebr, Try agian.")
            return get_number(v)
        else:
            return n
    except ValueError:
        print("Invalid input, Try again.")
        return get_number(v)

def gcd(a, b):
    
    foo = a
    bar = b
    tmp = 0
    while True:
        tmp = foo % bar
        if tmp == 0:
            break
        foo = bar
        bar = tmp
    return bar

def main():

    a = get_number('first')
    b = get_number('second')

    if a > b:
        print(gcd(a, b))
    else:
        print(gcd(b, a))

if __name__ == "__main__":
    main()

