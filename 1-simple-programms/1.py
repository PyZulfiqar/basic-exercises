import os

def calculate_square(n):
    return n * n

def main():
    number = input("Please Enter a number: ") 
    if number.isdigit():
        print(f"Square of {number} is {calculate_square(int(number))}")
    else:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(f"'{number}' is not a number, Try again!")
        main()

if __name__ == "__main__":
    main()