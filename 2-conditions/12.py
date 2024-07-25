import math

def get_known_number(value):

    try:
        n = float(input(f"Please Enter known number {value}: ")) 
        if value == 'a' and n == 0:
            print("In a Quadratic Equation a != 0, Please Try again.")
            return get_known_number(value)
        else:
            return n
    except ValueError:
        print("That's not number, Please try again!")
        return get_known_number(value) 

def calc_delta(a, b, c):

    return (b ** 2) - (4 * a * c)

def solve_equ(a, b, delta, sign):

    if sign == '+':
        return ((b * -1) + math.sqrt(delta)) / (2 * a)
    else:
        return ((b * -1) - math.sqrt(delta)) / (2 * a)

def main():

    a = get_known_number('a')
    b = get_known_number('b')
    c = get_known_number('c')

    print(f"Quadratic Equation: {a}*x**2 + {b}*x + {c}")

    delta = calc_delta(a, b, c)
    print(delta)
    if delta > 0:
        print("Equation have 2 answers!")
        print(f"root_1= {solve_equ(a, b, delta, '+')}")
        print(f"root_2= {solve_equ(a, b, delta, '-')}")
    elif delta == 0:
        print("Equation have 1 answer!")
        print(f"root= {solve_equ(a, b, delta, '+')}")
    else:
        print("Equation doesn't have any answers!")
    
if __name__ == "__main__":
    main()

