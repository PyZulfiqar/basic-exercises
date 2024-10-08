def get_input():

    try:
        return int(input("Please enter an Integer: "))
    except ValueError:
        print("That's not an integer, Try again!")
        return get_input()

number = get_input()

if number == 0:
    print("Not Prime")
    exit()

if number < 0:
    number = number * -1

c = 0
for i in range (1, number + 1):
    if number % i == 0:
        c = c + 1

if c == 2:
    print("Prime!")
else:
    print("Not Prime")