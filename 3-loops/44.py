foo = 0
bar = 1
i = 2
while (bar >= 0.0001):
    bar *= 1 / i
    if i % 2 == 0:
        foo += bar
    else:
        foo -= bar
    i += 1
print(foo)