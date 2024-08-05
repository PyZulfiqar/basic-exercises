def get_number():

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def check_avg(avg, current):

    if abs(avg - current) <= 1:
        return True
    else:
        return False

def main(): 

    sum_arr = 0
    my_arr = [None for i in range(50)]
    for i in range(50):
        my_arr[i] = get_number() 
        sum_arr += my_arr[i]
                
    avg = sum_arr / len(my_arr)
    
    c = 0
    for i in range(len(my_arr)):
        if check_avg(avg, my_arr[i]):
            c += 1
    print(c)

if __name__ == "__main__":
    main()