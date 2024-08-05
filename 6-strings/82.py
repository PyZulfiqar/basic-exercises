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
    to_list = [char for char in string]

    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
 
    for word in vowels:
        for i in range(len(to_list)):
            if to_list[i] == word:
                to_list[i] = ''
    
    print(''.join(to_list))

if __name__ == "__main__":
    main()