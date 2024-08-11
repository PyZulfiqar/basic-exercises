def get_name():
    
    while True:
        try:
            name = input()
            return name
        except ValueError:
            print("Invalid Input")

def main():

    string = ""
    for i in range(5):
        name = get_name()
        if name[0] == name[len(name) - 1]:
            string += name + "\n"
    print(string, end='')

if __name__ == "__main__":
    main()