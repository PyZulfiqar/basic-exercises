def get_name():
    
    while True:
        try:
            name = input()
            return name
        except ValueError:
            print("Invalid Input")

def find_min_len(a: str, b: str) -> tuple[str, str, int]:

    min_len: int 
    if len(a) < len(b):
        min_len = len(a)
    else:
        min_len = len(b)
    return a, b, min_len

def bubble_sort(arr: list[float]) -> list[float]:

    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            a, b, min_len = find_min_len(arr[j + 1], arr[j])
            for i in range(min_len):
                o_a = ord(a[i])
                o_b = ord(b[i])
                if o_a >= 97:
                    o_a -= 32
                if o_b >= 97:
                    o_b -= 32
                if o_a < o_b:
                    tmp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = tmp
                    break
                elif o_a > o_b:
                    break
    
    return arr


def main():

    names = [None for i in range(5)]
    for i in range(5):
        names[i] = get_name()

    sorted_names = bubble_sort(names)
    print(sorted_names)
if __name__ == "__main__":
    main()