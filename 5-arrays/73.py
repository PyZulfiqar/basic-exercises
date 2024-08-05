import os

def get_number(v: int) -> float:

    while True:
        try:
            n = float(input(f"Enter number {v}: ")) 
            os.system('cls' if os.name == 'nt' else 'clear')
            return n
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid Input.")

def bubble_sort(arr: list[float]) -> list[float]:

    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j + 1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    
    return arr


def main():

    os.system('cls' if os.name == 'nt' else 'clear')


    my_arr: list[float] = [0 for i in range(50)] 

    for i in range(0, len(my_arr)):
        my_arr[i] = get_number(i + 1)

    os.system('cls' if os.name == 'nt' else 'clear')

    sorted_arr = bubble_sort(my_arr)

    for i in range(0, len(sorted_arr)):
        print(sorted_arr[i])
    
if __name__ == "__main__":
    main()