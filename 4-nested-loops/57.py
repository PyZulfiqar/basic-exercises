import os

ansii = {
    "green": "\x1b[33m\x1b[1m",
    "red": "\x1b[31m\x1b[1m",
    "blue": "\x1b[34m\x1b[1m",
    "white_bg": "\x1b[107m",
    "reset": "\x1b[0m",
    "underline": "\x1b[4m\x1b[1m"
}

os.system('cls' if os.name == 'nt' else 'clear')
print("\n")

print(f"{ansii['white_bg']} {ansii['blue']}" +
      f"{'0':>5}{'1':>5}{'2':>5}{'3':>5}{'4':>5}"+
      f"{'5':>5}{'6':>5}{'7':>5}{'8':>5}{'9':>5} {ansii['reset']}", end='')
for i in range(0, 10):
    print(f"\n{ansii['white_bg']} {ansii['blue']}{'':<2}{ansii['reset']}")
    print(f"{ansii['white_bg']} {ansii['blue']}{str(i):<2}{ansii['reset']}", end='')
    for j in range(0, 10):
        print(f"{ansii['green']}{str(i * j):^5}", end='')

print("\n")
