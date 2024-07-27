total = 0
for i in range(1, 1001):
    if i % 2 == 0:
        #print(f"1/{i}+", end='')
        total += 1 / i
    else:
        #print(f"1/{i}-", end='')
        total -+ 1 / i
print()
print(total)