def get_number() -> float:

    while True:
        try:
            n = float(input())
            return n
        except ValueError:
            print("Invalid input.")

def find_rep(arr: list[float]):

    foo = arr[:]

    for i in range(len(arr)):
        c = 0
        tmp: float
        check = False
        for j in range(len(foo)):
            if arr[i] == foo[j]:
                c += 1
                tmp = arr[i]
                check = True

        if check:
            print(tmp, end = ' ') 

        bar = [None for j in range(len(foo) - c)] 
        index = 0

        for j in range(len(foo)):
            if foo[j] != tmp:
                bar[index] = foo[j]
                index += 1
        
        foo = bar[:]

def main(): 

    my_arr = [None for i in range(50)]
    
    for i in range(50):
        my_arr[i] = get_number() 

    find_rep(my_arr)

    print()


if __name__ == "__main__":
    main()