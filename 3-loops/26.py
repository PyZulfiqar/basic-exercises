def get_number():
    
    try:
        return int(input())
    except ValueError:
        return get_number()

n = get_number()
if n < 0:
    n = n * -1

c = 0
while(1):
    n = n / 10
    c = c + 1
    if n < 1:
        break
print(c)