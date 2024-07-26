sum = 0
for i in range(100):
    while True:
        try:
            n = float(input(f"Enter number {i + 1}: "))
            if n > 0:
                sum += n 
            break
        except ValueError:
           print("That's not a number, Try again.")
           continue 

print(sum)