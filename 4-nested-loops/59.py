ansii = {
    "yellow": "\x1b[33m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

for i in range(14, -1, -1):
    for j in range(0, i):
        print(f"  ", end='')
    print(f"{ansii['blue']}* {ansii['yellow']} * "+
          f"{ansii['blue']}* {ansii['yellow']} *")
