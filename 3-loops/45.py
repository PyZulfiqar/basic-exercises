def solve(x, i, t):

    if i % 2 != 0:
        t += (x ** i) / i
    else:
        t -= (x ** i) / i

    if abs((x ** (i + 1)) / (i + 1)) < 0.0001:
        return t
    else:
        i += 1
        return solve(x, i, t)

def get_x():
    try:
        x = float(input("Please Enter a decimal number:"))
        if abs(x) > 1:
            print("Please enter a number between -1 and +1, Try again.")
            return get_x()
        return x
    except ValueError:
        print("That's not a number, Please try again:")
        return get_x()

def main():
    x = get_x()
    total = solve(x, i=1, t=0)
    print(total)

if __name__ == "__main__":
    main()