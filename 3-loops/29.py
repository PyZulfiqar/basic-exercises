mult = 0
for i in range(100):
    while True:
        try:
            mult *= float(input(f"Enter number {i + 1}: "))
            break
        except ValueError:
           print("That's not a number, Try again.")
           continue 
print(mult)