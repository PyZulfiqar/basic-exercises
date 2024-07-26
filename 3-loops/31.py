c = 0
for i in range(100):
    while True:
        try:
            n = float(input(f"Enter number {i + 1}: "))
            if n > 0:
                c += 1 
            break
        except ValueError:
           print("That's not a number, Try again.")
           continue 

print(c)