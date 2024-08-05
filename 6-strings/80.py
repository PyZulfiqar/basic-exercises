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

def get_char() -> str:

    while True:
        try:
            name = input(f"Enter character: ")
            if len(name) != 1:
                print("Invalid input") 
            else: 
                return name
        except ValueError:
            print("Invalid input")


def main():

    name = get_name()
    char = get_char()

    c = 0

    for ch in name:
        if ch == char:
            c += 1
    print(c)

if __name__ == "__main__":
    main()