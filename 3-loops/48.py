def check_avg(avg):

    if 10 < avg < 15:
        return True
    else:
        return False

def get_n():

    try:
        n = int(input("Enter the number of the students: "))
        if n < 0:
            print("Invalid number, Try again.")
            return get_n()
        else:
            return n
    except ValueError:
        print("Invalid input, Try again.")
        return get_n()

def get_avg(i):

    try:
        avg = float(input(f"Enter student {i}'s grade average: "))
        if avg < 0 or avg > 20:
            print("Invalid grade average, Try again.")
            return get_avg(i) 
        else:
            return avg 
    except ValueError:
        print("Invalid input, Try again.")
        return get_avg(i)



def main():
    
    n = get_n()

    c = 0
    for i in range(1, n + 1):
        avg = get_avg(i)
        if check_avg(avg):
            c += 1
    
    print(f"Number of grade averages between 10 and 15: {c}")

if __name__ == "__main__":
    main()