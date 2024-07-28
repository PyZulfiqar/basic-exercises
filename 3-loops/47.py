def solve(x, i, s, t):

    if s:
        t += (x ** i) / factorial(i)
        s = False
    else:
        t -= (x ** i) / factorial(i)
        s = True
    
    if abs((x ** (i + 1)) / factorial(i + 1)) < 0.0001:
        return t
    else:
        i += 2
        return solve(x, i, s, t)
    

def factorial(n):

    s = False
    if n < 0:
        n = -1 * n
        s = True
    
    c = 1
    for i in range(1, n + 1):
        c *= i
    
    if s:
        return -1 * c
    else:
        return c


def get_x():

    try:
        x = float(input("Enter a number between -1 and +1: "))
        if abs(x) >= 1:
            print(f"{x} is not a number between -1 and +1:")
            return get_x()
        else:
            return x
    except ValueError:
        print(f"That's not a number, Try again.")
        return get_x()

def main():
    x = get_x() 

    t = solve(x, i = 1, s = True, t = 0)

    print(t)

if __name__ == "__main__":
    main()