def get_char():
    char = input("Please Enter a character: ")
    if len(char) > 1:
        print("That's not a character, Please Try again!")
        return get_char()
    elif len(char) == 0:
        print("Seems like nothing's there, Please Try again!")
        return get_char()
    else:
        return char

def main():

    char = get_char()
    # ord() and chr()
    char_ascii = ord(char)

    print(f"Character: {char}\nASCII: {char_ascii}")

if __name__ == "__main__":
    main()