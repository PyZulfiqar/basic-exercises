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

def check_type(char):

    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        if (ord(char) == 65 or ord(char) == 97 
            or ord(char) == 69 or ord(char) == 101
            or ord(char) == 73 or ord(char) == 105
            or ord(char) == 79 or ord(char) == 111
            or ord(char) == 85 or ord(char) == 117):
            return 'Vowel'
        else:
            return 'Consonants'
    elif 48 <= ord(char) <= 57:
        return 'Digit'
    else:
        return 'Other'

char = get_char()
foo = check_type(char)
print(f"{char} is {'a' if foo != 'Other' else 'an'} '{foo}'")