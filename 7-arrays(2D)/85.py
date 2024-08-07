import os

ansii = {
    "reset": "\x1b[0m",
    "green": "\x1b[1m\x1b[32m",
    "red": "\x1b[1m\x1b[31m",
}

def get_number(i: int, j: int) -> int:

    while True:
        try:
            number = int(input(f"{ansii['green']}Enter element [{i},{j}]: {ansii['reset']}"))
            return number
        except ValueError:
            print(f"{ansii['red']}Not an integer.{ansii['reset']}")

def get_matrix() -> tuple[list, int]:

    m: list[list[int]] = [None for i in range(3)]

    sum_e = 0
    for i in range(3):
        tmp_a = [None for i in range(4)]
        m[i] = tmp_a
        for j in range(4):
            m[i][j] = get_number(i + 1, j + 1)
            sum_e = m[i][j]
    
    return m, sum_e
 
def show_matrix(m: list[list]) -> str:

    string = ansii["green"]
    for i in range(len(m)):
        for j in range(len(m[0])):
            string += f"{m[i][j]:^5}"
        string += '\n'
    string += ansii["reset"]

    return string



def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    m, sum_e = get_matrix()

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{ansii['green']}3x4 matrix:{ansii['reset']}")
    print(show_matrix(m), end='')

    print(f"{ansii['green']}Sum of the elements: {sum_e}{ansii['reset']}")
    


if __name__ == "__main__":
    main()