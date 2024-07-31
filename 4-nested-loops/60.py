ansii = {
    "yellow": "\x1b[33m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

for i in range(15):
    for j in range(15):
        print("  ", end='')
    for j in range(i):
        if j % 2 == 0:
            print(f"{ansii['blue']}* ", end='')
        else:
            print(f"{ansii['yellow']}* ", end='')
    print()