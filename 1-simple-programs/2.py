import os

p = 3.14

def solve_area(r):
    return p * r ** 2

def solve_perimeter(r):
    return 2 * p * r

def get_input():
    
    try:
        r = int(input("Please Enter Radius: "))
        if r <= 0:
            os.system('cls' if os.name == "nt" else "clear")
            print(f"A circle can't have radius of {r}! please try again!")
            return get_input()
        else:
            return r
    
    except ValueError:
        os.system('cls' if os.name == "nt" else "clear")
        print(f"That's not a number, please try again!")
        return get_input()

def main():

    radius = get_input() 
    area = solve_area(radius)
    perimeter = solve_perimeter(radius)

    print(f"Perimeter: {perimeter}\nArea: {area}")

if __name__ == "__main__":
    main()