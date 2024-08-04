def get_number() -> float:

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def find_max(arr: list[float]) -> float:

    arr_max = 0
    for number in arr:
        if number >= arr_max:
            arr_max = number
    
    return arr_max

def add_difference(arr: list[float], arr_max: float) -> list[float]:

    d = 20 - arr_max
    print(arr_max)
    print(d)

    for i in range(len(arr)):
        arr[i] += d
    return arr

def main(): 

    my_arr = [None for i in range(50)]
    for i in range(50):
        my_arr[i] = get_number() 

    arr_max = find_max(my_arr)
    new_arr = add_difference(my_arr, arr_max)

    for grade in new_arr:
        print(grade, end=' ')
    print()
                
    

if __name__ == "__main__":
    main()