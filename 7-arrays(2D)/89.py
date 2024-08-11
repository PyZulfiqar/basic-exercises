import os

ansii = {
    "reset": "\x1b[0m",
    "yellow": "\x1b[93;1m",
    "white": "\x1b[97;1m",
    "red": "\x1b[91;1m",
    "green": "\x1b[32;1m",
    "light_blue": "\x1b[94;1m",
    "red": "\x1b[31;1m",
    "white_b": "\x1b[47;30;1m"
}

def get_elements(text) -> int:

    while True:
        try:
            element = int(input(text))
            if element < 0:
                print(f"{ansii['red']}Invalid number.{ansii['reset']}")
            else:
                return element 
        except ValueError:
            print(f"{ansii['red']}Not an integer.{ansii['reset']}")

def get_matrix(a: int, b: int) -> list[list]:

    m: list[list[int]] = [None for i in range(a)]

    for i in range(a):
        tmp_a = [None for i in range(b)]
        m[i] = tmp_a
        for j in range(b):
            if j == 0:
                m[i][j] = get_elements(f"{ansii['green']}{i + 1360} gold medals: {ansii['reset']}")
            elif j == 1:
                m[i][j] = get_elements(f"{ansii['green']}{i + 1360} silver medals: {ansii['reset']}")
            else:
                m[i][j] = get_elements(f"{ansii['green']}{i + 1360} bronze medals: {ansii['reset']}")
    
    return m

def show_matrix(m: list[list], v: bool) -> tuple[str, int]:

    y = "Year"
    g = 'Gold'
    s = "Silver"
    b = 'Bronze'
    so = "Score"
    c = 0

    if v:
        string = f"{ansii['white_b']}{y:^8}{so:^8}\n{ansii['reset']}" 
    else:
        string = f"{ansii['white_b']}{y:^8}{g:^8}{s:^8}{b:^8}\n{ansii['reset']}" 
    for i in range(len(m)):
        string += f"{ansii['light_blue']}{str(i + 1360):^8}"
        score = 0
        for j in range(len(m[i])):
            if j == 0:
                score += m[i][j] * 3
                if not v:
                    string += f"{ansii['yellow']}{m[i][j]:^8}"
            elif j == 1:
                score += m[i][j] * 2
                if not v:
                    string += f"{ansii['white']}{m[i][j]:^8}"
            elif j == 2:
                score += m[i][j]
                if not v:
                    string += f"{ansii['red']}{m[i][j]:^8}"
                if v:
                    string += f"{ansii['green']}{score:^8}"
        if score > 10:
            c += 1 
        string += '\n'
    string += ansii["reset"]

    return string, c

def find_all(m: list[list]):

    sum_all = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            sum_all += m[i][j]
    return sum_all

def all_gold(m: list[list]):

    sum_gold = 0
    for i in range(len(m)):
        sum_gold += m[i][0]
    
    return sum_gold

def no_medals(m: list[list]):

    string = f"{ansii['light_blue']}"
    for i in range(len(m)):
        sum_medal = 0
        for j in range(len(m[i])):
            sum_medal += m[i][j]
        if sum_medal == 0:
            string += f"{i + 1360} " 
    string += f"{ansii['reset']}"
    return string

def max_medal(m: list[list]):

    max_m = 0
    max_y = 0
    for i in range(len(m)):
        sum_m = 0
        for j in range(len(m[i])):
            sum_m += m[i][j]
        if max_m <= sum_m:
            max_m = sum_m
            max_y = i + 1360
    
    return max_y
            
def max_gold(m: list[list]):

    max_m = 0
    max_y = 0
    for i in range(len(m)):
        if max_m <= m[i][0]:
            max_m = m[i][0]
            max_y = i + 1360
    
    return max_y

def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    medals = get_matrix(31, 3)

    os.system('cls' if os.name == 'nt' else 'clear')

    string, c =show_matrix(medals, False)
    print(string)

    sum_all = find_all(medals)
    print(f"{ansii['light_blue']}A) Total Medals: {sum_all}{ansii['reset']}")

    sum_gold = all_gold(medals)
    print(f"{ansii['light_blue']}B) Total Golds: {sum_gold}{ansii['reset']}")

    print(f"{ansii['light_blue']}C) No Medals: {no_medals(medals)}{ansii['reset']}")

    max_year = max_medal(medals)
    print(f"{ansii['light_blue']}D) Most Medal: {max_year}{ansii['reset']}")

    max_g = max_gold(medals)
    print(f"{ansii['light_blue']}E) Most Gold: {max_g}{ansii['reset']}")

    string, c =show_matrix(medals, True)
    print(f"{ansii['light_blue']}F) Scores: {ansii['reset']}")
    print(string, end = '')
    print(f"{ansii['light_blue']}G) Scores > 10: {c}{ansii['reset']}\n")



if __name__ == "__main__":
    main()