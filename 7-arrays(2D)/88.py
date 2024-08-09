import os

ansii = {
    "reset": "\x1b[0m",
    "green": "\x1b[1m\x1b[32m",
    "red": "\x1b[1m\x1b[31m",
}

def get_elements(text) -> int:

    while True:
        try:
            element = int(input(text))
            return element 
        except ValueError:
            print(f"{ansii['red']}Not an integer.{ansii['reset']}")

def get_number(v: str) -> int:

    while True:
        try:
            number = int(input(f"{ansii['green']}Enter {v}: {ansii['reset']}"))
            if 0 < number <= 10:
                return number
            else:
                print(f"{ansii['red']}{v} is 0 < {v} < 11, Try again.{ansii['reset']}")
        except ValueError:
            print(f"{ansii['red']}Not an integer.{ansii['reset']}")

def get_matrix(a: int, b: int, string: str) -> list[list]:

    m: list[list[int]] = [None for i in range(a)]

    for i in range(a):
        tmp_a = [None for i in range(b)]
        m[i] = tmp_a
        for j in range(b):
            m[i][j] = get_elements(f"{ansii['green']}Enter element [{i + 1},{j + 1}] of the {string} matrix: {ansii['reset']}")
    
    return m

def show_matrix(m: list[list]) -> str:

    string = ansii["green"]
    for i in range(len(m)):
        for j in range(len(m[i])):
            string += f"{m[i][j]:^5}"
        string += '\n'
    string += ansii["reset"]

    return string

def find_t(m: list[list]) -> list[list]:
    
    t: list[list[int]] = [None for i in range(len(m[0]))]

    for j in range(len(m[0])):
        tmp_a = [None for i in range(len(m))]
        t[j] = tmp_a
        for i in range(len(m)):
            t[j][i] = m[i][j]
    
    return t


def mult_m(a, b):

    m: list[list[int]] = [None for i in range(len(a))]
    for i in range(len(m)):
        tmp_a = [None for i in range(len(b[0]))]
        m[i] = tmp_a
    
    t_b = find_t(b)

    for i in range(len(a)):
        foo = a[i]
        for j in range(len(t_b)):
            bar = t_b[j]
            mult = 0
            for k in range(len(foo)):
                mult += foo[k] * bar[k]
            m[i][j] = mult
    
    return m

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    m = get_number('m')
    n = get_number('n')
    p = get_number('p')

    m_1 = get_matrix(m, n, "first")
    m_2 = get_matrix(n, p, "second")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{ansii['green']}{m}x{n} matrix:{ansii['reset']}")
    print(show_matrix(m_1), end='')
    print(f"{ansii['green']}{n}x{p} matrix:{ansii['reset']}")
    print(show_matrix(m_2), end='')

    m_m = mult_m(m_1, m_2)
    print(f"{ansii['green']}{n}x{p} Result:{ansii['reset']}")
    print(show_matrix(m_m), end='')

if __name__ == "__main__":
    main()