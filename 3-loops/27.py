def get_number():

    try:

        n = int(input())
        return n if n > 0 else get_number()
    
    except ValueError:

        return get_number()

n = get_number()

foo = 0
while (n > 0):
    
    foo += n % 10
    n //= 10

print(foo)