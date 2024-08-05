def get_string() -> str:

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

    string = get_string()
    new_str = ""
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
 
    for i in range(len(string)):
        check = True
        for word in vowels:
            if string[i] == word:
                check = False
        if check:
            new_str += string[i]
    
    print(new_str)

if __name__ == "__main__":
    main()