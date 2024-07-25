import os

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

def check_type(a, b, c):

    if a == b == c:
        return "Equilateral"
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return "Isosceles"
    elif a != b and a != c and b != c:
        return "Scalene"
    else:
        return "Error"


def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    a = get_side("first") 
    b = get_side("second")
    c = get_side("third")

    type = check_type(a, b , c)
    print(f"a= {a}, b= {b}, c = {c}")
    print(f"This triangle is a '{type}'!")



if __name__ == "__main__":
    main()