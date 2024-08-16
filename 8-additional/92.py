import os

def get_number(v: int) -> float:

    while True:
        try:
            number = float(input(f"\x1b[32;1mEnter Number {v}: \x1b[0;1m"))
            return number
        except ValueError:
            print(f"\x1b[31;1mInvalid input.\x1b[0m")

def avg(arr: list[float]) -> float:

    sum_arr = 0
    for i in range(len(arr)):
        sum_arr += arr[i]
    avg_arr = sum_arr / len(arr)

    return avg_arr

def find_closest(avg_arr: float, arr: list[float]) -> float:

    target = arr[0]
    dif = abs(avg_arr - target)
    for i in range(1, len(arr)):
        if abs(avg_arr - arr[i]) < dif:
            target = arr[i] 
            dif = abs(avg_arr - arr[i])
    
    return target

def main():
    
    os.system('cls' if os.name == 'nt' else 'clear')

    numbers = [None for i in range(5)]
    for i in range(len(numbers)):
        numbers[i] = get_number(i + 1)

    avg_numbers = avg(numbers)
    closest = find_closest(float(avg_numbers), numbers)
    f"{avg_numbers:.2f}"
    print("\x1b[47;30;1m{0:<15}{1:<1}\x1b[0m".format("Average", "Closest"))
    print(f"\x1b[33;1m{avg_numbers:<15}{closest}\x1b[0m")

if __name__ == "__main__":
    main()