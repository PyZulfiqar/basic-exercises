def get_n():

    try:
        n = int(input("Please enter n: "))
        if n < 1:
            print("Invalid numebr, Try agian.")
            return get_n()
        else:
            return n
    except ValueError:
        print("Invalid input, Try again.")
        return get_n()

def get_numbers(i):

    try:
        n = float(input(f"Please enter float number {i}: "))
        return n
    except ValueError:
        print("Invalid input, Try again.")
        return get_n(i)

def main():
    
    n = get_n()
    foo = 0
    bar = 0
    for i in range(n):
        tmp = get_numbers(i+1)
        foo += tmp ** 2
        bar += tmp
    
    v = (foo / n) - ((bar / n) ** 2)

    print(v)

if __name__ == "__main__":
    main()