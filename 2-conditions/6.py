def calc_remainder(n):
    return n % 2

def get_number():
    try:
        return int(input("Please Enter a number: "))
    except ValueError:
        print("That's not an integer, Please try again!")
        return get_number()

def main():
    n = get_number()
    r = calc_remainder(n)
    if r == 0:
        print(f"{n} is even!")
    else:
        print(f"{n} is odd!")

if __name__ == "__main__":
    main()