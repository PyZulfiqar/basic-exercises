def get_number():

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def main():
   
    my_arr = [None for i in range(50)]
    for i in range(50):
        my_arr[i] = get_number() 
    
    for i in range(len(my_arr) - 1, -1):
        print(my_arr[i])


if __name__ == "__main__":
    main()