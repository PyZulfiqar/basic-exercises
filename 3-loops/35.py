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

def check_max_avg(max_avg, new_avg):

    if new_avg >= max_avg:
        return new_avg
    else:
        return max_avg


def main():

    max_avg = 0
    for i in range(1, 6):
        new_avg = get_avg_grade(i)
        max_avg = check_max_avg(max_avg, new_avg) 

    print(f"The maximum grade average is: {max_avg}")

if __name__ == "__main__":
    main()