def solve_area(w, l):
    return w * l

def solve_perimeter(w, l):
    return 2 * (w + l)

def get_input(value):
    
    try:
        number = int(input(f"Please Enter {value}: "))
        if number <= 0:
            print(f"A Rectangle can't have a such side! please try again!")
            return get_input('width' if value=='width' else 'height')
        else:
            return number
    
    except ValueError:
        print(f"That's not a number, please try again!")
        return get_input('width' if value=='width' else 'height')


def main():

    width = get_input('width')
    lenght = get_input('lenght')

    area = solve_area(width, lenght)
    perimeter = solve_perimeter(width, lenght)
    
    print(f"Width={width} and lenght={lenght}\n")
    print(f"Area: {area}\nPerimeter: {perimeter}")

if __name__ == "__main__":
    main()