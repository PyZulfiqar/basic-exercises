total = 0
for i in range(1, 101, 2):
    mult = i * (i + 1)
    sum = i + (i + 1)
    #print(f"{i}x{i+1}/{i}+{i+1} + ", end= '')
    total += mult / sum
print(total)