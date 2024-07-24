def get_number(index):

    try:
        return int(input(f"Please enter number {index}: "))
    except ValueError:
        return get_number(index)

def calc_avg(a, b, c):

    return (a + b + c) / 3

def main():

   a = get_number(1) 
   b = get_number(2)
   c = get_number(3)
   avg = calc_avg(a, b, c)
   print(f"({a} + {b} + {c}) / 3 = {avg}")

if __name__ == "__main__":
    main()