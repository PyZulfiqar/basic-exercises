def get_input():

    try:
        return int(input("Please enter an Integer: "))
    except ValueError:
        print("That's not an integer, Try again!")
        return get_input()

number = get_input()
if number <= 0:
    print(f"No Natural number exist below or equal to '{number}'!")
else:
    for i in range(1, number + 1):
        print(i)