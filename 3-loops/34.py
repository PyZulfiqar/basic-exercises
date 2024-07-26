def get_number():
    try:
        return int(input())
    except ValueError:
        return get_number()

def factorial(n):

    c = 1
    for i in range(1, n + 1):
        c *= i
    
    return c

def main():

    number = get_number()
    neg_stat = False
    if number < 0:
        number *= -1
        neg_stat = True

    fac = factorial(number)

    print(fac if neg_stat == False else fac * -1)

if __name__ == "__main__":
    main()