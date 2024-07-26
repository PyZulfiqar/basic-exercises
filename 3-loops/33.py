pos_sum = 0
pos_c = 0
neg_sum = 0
neg_c = 0
for i in range(100):
    while True:
        try:
            n = float(input(f"Enter number {i + 1}: "))
            if n > 0:
                pos_sum += n 
                pos_c += 1
            elif n < 0:
                neg_sum += n
                neg_c += 1
            break
        except ValueError:
           print("That's not a number, Try again.")
           continue 

if pos_c > 0:
    print(f"positive avg = {pos_sum / pos_c}")
if neg_c > 0:
    print(f"negative avg = {neg_sum / neg_c}")