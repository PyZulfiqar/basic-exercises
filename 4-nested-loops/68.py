def get_number() -> float:

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def calc_avg(arr: list[float]) -> float:

    sum_arr = 0
    for grade in arr:
        sum_arr += grade 
    avg: float = sum_arr / len(arr)

    return avg 

def a_d(arr: list[float], avg: float) -> float:

    foo = 0
    for grade in arr:

        foo += abs(grade - avg)
    
    bar = foo / len(arr)

    return bar

def main(): 

    my_arr = [None for i in range(50)]
    for i in range(50):
        my_arr[i] = get_number() 

    avg = calc_avg(my_arr)
    ad = a_d(my_arr, avg)

    print(ad)

if __name__ == "__main__":
    main()