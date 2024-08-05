def get_name(v: int) -> str:

    while True:
        try:
            name = input(f"Enter name {v}: ")
            if len(name) == 0:
                print("Invalid input") 
            else: 
                return name
        except ValueError:
            print("Invalid input")

def main():

    max_l = 0
    max_n = ""
    for i in range(5):
        name = get_name(i + 1)
        if len(name) >= max_l:
            max_l = len(name) 
            max_n = name
    
    print(max_n)




if __name__ == "__main__":
    main()