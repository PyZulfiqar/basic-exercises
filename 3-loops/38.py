def get_avg_grade(number):

    try:
        avg_grade = float(input(f"Enter student {number}'s average grade: "))
        if avg_grade < 0:
            print(f"An average grade can't be a negative number, Try again.")
            return get_avg_grade(number)
        elif avg_grade > 20:
            print(f"An average grade can't be a more than 20, Try again.")
            return get_avg_grade(number)
        else:
            return avg_grade
    except ValueError:
        print("That's not a number, Try again.")
        return get_avg_grade(number)

def check_above_fifteen(avg):

    if avg > 15:
        return True
    else:
        return False


def main():

    c = 0
    sum = 0
    for i in range(1, 6):
        new_avg = get_avg_grade(i)
        if check_above_fifteen(new_avg):
            sum += new_avg
            c += 1

    foo = "No above 15"
    print(f"Average of grade averages above 15: {sum / c if c > 0 else foo}")

if __name__ == "__main__":
    main()