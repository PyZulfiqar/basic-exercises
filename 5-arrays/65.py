def get_number():

    try:
        n = float(input())
        return n
    except ValueError:
        print("Invalid input.")
        return get_number()

def check_min(current, last):

    if current < last:
        return True
    else:
        return False

def main():
   
    my_arr = [None for i in range(50)]
    for i in range(50):
        my_arr[i] = get_number() 
    
    c = 0
    for i in range(len(my_arr)):
        if check_min(current=my_arr[i], last=my_arr[len(my_arr) - 1]):
            c += 1
    
    print(c)

if __name__ == "__main__":
    main()