def get_number():

    try:
        n = int(input())
        if n < 1:
            print("Invalid number")
            return get_number()
        else:
            return n
    except ValueError:
        print("Invalid input")
        return get_number()

def check_prime(n):

    for i in range(2, n + 1):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1 
        if c == 2 and n % i == 0:
            return i 
        
def divide_prime(n):

    p = check_prime(n)
    n = n // p

    if n == 1:
        print(f"{p}")
        return False, n
    else:
        print(f"{p} x ", end='')
        return True, n

def main():

    n = get_number()
    check = True

    while check:

        check, n = divide_prime(n)




if __name__ == "__main__":
    main()
