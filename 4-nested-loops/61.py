ansii = {
    "yellow": "\x1b[33m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

c = 1
for i in range(15, 0, -1):
    for j in range(i):
        print("  ", end='')
    for j in range(c):
        if j % 2 == 0:
            print(f"{ansii['blue']}* ", end='')
        else:
            print(f"{ansii['yellow']}* ", end='')
    c += 2
    print()