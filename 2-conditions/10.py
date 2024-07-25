def get_month(message):

    try:
        m = int(input(f"{message}")) 
        return m if 0 < m < 13 else get_month("Please enter a valid number, try again: ") 
    except ValueError:  
        return get_month("That's not a number! Please try again: ")

def show_days(month):

    if 0 < month < 6:
        return 31
    elif 5 < month < 12:
        return 30
    else:
        return 29

month = get_month("Please Enter a month's number: ")
days = show_days(month)

print(f"Month number {month} has {days} days!")