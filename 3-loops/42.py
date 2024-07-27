odd = 1
even = 1

for i in range(1, 101, 2):
    odd *= i
    #print(odd)
    even *= i + 1
    #print(even)

result = odd / even
print(result)