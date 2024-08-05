def get_string() -> str:

    while True:
        try:
            return input() 
        except ValueError:
            print("Invalid input")

def main():
    
    c = 0
    while True:

        tmp = get_string()
        if tmp == 'finish':
            break
        for char in tmp:
            if 48 <= ord(char) <= 57:
                c += 1
                break
        
    print(c)
    
            
if __name__ == "__main__":
    main()