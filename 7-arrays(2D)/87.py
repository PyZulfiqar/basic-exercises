import os

ansii = {
    "reset": "\x1b[0m",
    "green": "\x1b[1m\x1b[32m",
    "red": "\x1b[1m\x1b[31m",
}

def get_number(text) -> int:

    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print(f"{ansii['red']}Not an integer.{ansii['reset']}")

def get_matrix(n: int) -> list[list]:

    m: list[list[int]] = [None for i in range(n)]

    for i in range(n):
        tmp_a = [None for i in range(n)]
        m[i] = tmp_a
        for j in range(n):
            m[i][j] = get_number(f"{ansii['green']}Enter element [{i + 1},{j + 1}]: {ansii['reset']}")
    
    return m

def show_matrix(m: list[list]) -> str:

    string = ansii["green"]
    for i in range(len(m)):
        for j in range(len(m[0])):
            string += f"{m[i][j]:^5}"
        string += '\n'
    string += ansii["reset"]

    return string

def first_row(m: list[list]):

    sum_row = 0
    for i in range(len(m[0])):
        sum_row += m[0][i]

    return sum_row

def last_row(m: list[list]):

    mult_row = 1
    for i in range(len(m[len(m) - 1])):
        mult_row *= m[len(m) - 1][i]
    
    return mult_row

def main_diagonal(m: list[list]):

    max_e = 0
    for i in range(len(m)):
        if max_e <= m[i][i]:
            max_e = m[i][i]
    return max_e

def secondary_diagonal(m: list[list]):

    c = 0
    j = len(m) - 1
    for i in range(len(m)):
        if m[i][j] == 0:
            c += 1
        j -= 1
    
    return c

def neg_ele(m: list[list]):

    c = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] < 0:
                c += 1
    
    return c

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    n: int
    while True:
        n = get_number(f"{ansii['green']}Enter n: {ansii['reset']}")
        if 0 < n <= 10:
            break
        else:
            print(f"{ansii['red']}n is 0 < n < 11, Try again.{ansii['reset']}")
    m = get_matrix(n)

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{ansii['green']}{n}x{n} matrix:{ansii['reset']}")
    print(show_matrix(m), end='')

    a = first_row(m)
    print(f"{ansii['green']}A) Sum of first row's elements: {a}{ansii['reset']}")   

    b = last_row(m)
    print(f"{ansii['green']}B) Multiplication of last row's elements: {b}{ansii['reset']}")

    c = main_diagonal(m)
    print(f"{ansii['green']}C) Greatest main diagonal element: {c}{ansii['reset']}")

    d = secondary_diagonal(m)
    print(f"{ansii['green']}D) Number of zeros in the secondary diagonal: {d}{ansii['reset']}")

    e = neg_ele(m)
    print(f"{ansii['green']}E) Number of negative elements in the matrix: {e}{ansii['reset']}")
    


if __name__ == "__main__":
    main()