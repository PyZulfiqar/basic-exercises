def get_number() -> float:

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def find_rep(arr: list[float]):

    foo = arr[:]

    max_number: int
    max_number_rep: int = 0

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
            if c >= max_number_rep :
                max_number_rep = c
                max_number = tmp
            #print(f"{tmp}: {c}") 
        bar = [None for j in range(len(foo) - c)] 
        index = 0

        for j in range(len(foo)):
            if foo[j] != tmp:
                bar[index] = foo[j]
                index += 1
        
        foo = bar[:]
    
    return max_number, max_number_rep

def main(): 

    my_arr = [None for i in range(50)]
    
    for i in range(50):
        my_arr[i] = get_number() 

    max_number, max_rep = find_rep(my_arr)

    print(max_number, max_rep)


if __name__ == "__main__":
    main()