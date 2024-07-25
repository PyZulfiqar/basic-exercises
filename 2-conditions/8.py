import os
import math

def get_side(value):

    try:
        side = float(input(f"Please Enter {value} side: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if side <= 0 :
            print("A triangle can't have such side! Please Try again!")
            return get_side(value)
        else:
            return side
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("That's not a number! Please try again.")
        return get_side(value)

def calc_hypo(x , y):

    return math.sqrt(x ** 2 + y ** 2) 

def check_right(a, b, c):

    if a == calc_hypo(b , c):
        return True, b, c
    elif b == calc_hypo(a , c):
        return True, a, c
    elif c == calc_hypo(a , b):
        return True, a, b
    else:
        return False, None, None

def calc_area(b, h):

    return (b * h) / 2

def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    a = get_side("first") 
    b = get_side("second")
    c = get_side("third")

    check, base, height = check_right(a, b , c)

    if check:
        print("It's a Right Triangle!")
        print(f"Area= {calc_area(base, height)}")
    else:
        print("It's not a Right Triangle.")
        print(f"Perimeter= {a + b + c}")

if __name__ == "__main__":
    main()