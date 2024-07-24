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
            print("A circle can't have radius of {r}! please try again!")
            get_input()
        else:
            return r
    
    except(ValueError):
        os.system('cls' if os.name == "clear" else "cls")
        print(f"'{r}' is not a number, please try again!")
        get_input()

def main():
    ...

if __name__ == "__main__":
    main()