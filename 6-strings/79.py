def get_name() -> str:

    while True:
        try:
            name = input(f"Enter name: ")
            if len(name) == 0:
                print("Invalid input") 
            else: 
                return name
        except ValueError:
            print("Invalid input")

def main():

    name = get_name()
    print(name[len(name) - 1]) 



if __name__ == "__main__":
    main()