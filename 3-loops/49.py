import os

def get_number():
    try:
        foo = float(input("Enter a number between -1 and +1: "))
        if 0 <= abs(foo) < 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return foo
        else: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid number, Try again")
            return get_number()
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid input, Try again")
        return get_number()

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    c = 0
    sum_pos = 0
    while True:
        number = get_number()
        if number < 0:
            break
        else:
            sum_pos += number
            c += 1   
    
    avg = sum_pos / c if c > 0 else 'No positive numbers' 

    print(f"The average of the positive numbers: {avg}")

if __name__ == "__main__":
    main()