import os

ansii = {
    "reset": "\x1b[0m",
    "green": "\x1b[32;1m",
    "white": "\x1b[37;1m",
    "yellow": "\x1b[33;1m",
    "blue": "\x1b[34;1m",
    "red": "\x1b[31;1m",
    "white_bg": "\x1b[47;30;1m"
}

def get_name(i: int) -> str:
    
    while True:
        try:
            name = input(f"{ansii['green']}Enter athlete {i}'s name: {ansii['reset']}")
            return name
        except ValueError:
            print(f"{ansii['red']}Invalid Input, Try again.{ansii['reset']}")

def get_score(i: int, n: str) -> float:
    
    while True:
        try:
            score = float(input(f"{ansii['green']}Enter referee {i}'s score for {n}: {ansii['reset']}"))
            return score
        except ValueError:
            print(f"{ansii['red']}Invalid Input, Try again.{ansii['reset']}")

def get_athletes() -> tuple[list, list]:

    # array to hold athlete names
    names: list = [None for i in range(100)] 

    # 2D-array for athelet scores
    athletes: list[list] = [None for i in range(100)]
    for i in range(len(athletes)):
        athletes[i] = [None for i in range(10)]
       
    for i in range(len(athletes)):
        names[i] = get_name(i + 1)
        for j in range(len(athletes[i])):
            athletes[i][j] = get_score(j + 1, names[i])
    
    return names, athletes

def dif_avg(athletes: list):

    dif_arr = [None for i in range(len(athletes))]
    ref_arr = [None for i in range(len(athletes))]
    avg_arr = [None for i in range(len(athletes))]

    for i in range(len(athletes)):
        avg = 0
        for j in range(len(athletes[i])):
            avg += athletes[i][j]
        avg /= len(athletes[i]) 
        avg_arr[i] = avg
        max_dif = 0
        max_ref = 0
        for j in range(len(athletes[i])):
            tmp_dif = athletes[i][j] - avg 
            if tmp_dif > max_dif:
                max_dif = tmp_dif
                max_ref = j
        dif_arr[i] = max_dif
        ref_arr[i] = max_ref

    return dif_arr, ref_arr, avg_arr

def find_max(dif_arr, ref_arr):
    
    max_dif = 0
    max_ath = 0
    max_ref = 0
    for i in range(len(dif_arr)):
        #print(dif_arr[i])
        #print(ref_arr[i])
        if dif_arr[i] > max_dif:
            max_dif = dif_arr[i]
            max_ath = i
            max_ref = ref_arr[i]
    
    return max_ath, max_ref

def show_res(names: list[str], athletes: list[float], dif_arr: list[float], ref_arr: list[int], avg_arr: list[float]):
    
    string = f"{ansii['white_bg']}{'Number':^10}{'Name':^10}"
    for i in range(len(athletes[0])):
        tmp = "Refree" + str(i + 1)
        string += f"{tmp:^10}"
    string += f"{'avg':^10}{'dif avg':^10}{'target ref':^10}{ansii['reset']}\n"

    string += f"{ansii['blue']}"
    for i in range(len(athletes)):
        string += f"{str(i + 1):^10}"
        string += f"{names[i]:^10}"
        for j in range(len(athletes[i])):
            string += f"{str(athletes[i][j]):^10}"
        tmp = f"{avg_arr[i]:.2f}"
        string += f"{tmp:^10}"
        tmp = f"{dif_arr[i]:.2f}"
        string += f"{tmp:^10}"
        string += f"{str(ref_arr[i] + 1):^10}\n"
    string += f"{ansii['reset']}"

    return string
    
def real_champion(athletes):

    avg_arr = [None for i in range(len(athletes))]
    for i in range(len(athletes)):
        avg = 0
        for j in range(len(athletes[i])):
            avg += athletes[i][j]
        avg /= (len(athletes[i]) - 1)
        avg_arr[i] = avg
    
    max_avg = 0
    max_ath = 0
    for i in range(len(avg_arr)):
        if avg_arr[i] > max_avg:
            max_avg = avg_arr[i]
            max_ath = i
    
    return max_ath

def remove_cheaters(ath, ref, athletes):

    for i in range(len(athletes)):
        athletes[i][ref] = 0
    
    for i in range(len(athletes[ath])):
        athletes[ath][i] = 0

    return athletes



def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    names, athletes = get_athletes()
    
    dif_arr, ref_arr, avg_arr = dif_avg(athletes)

    max_ath, max_ref = find_max(dif_arr, ref_arr)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(show_res(names, athletes, dif_arr, ref_arr, avg_arr))

    print(f"{ansii['red']}Cheater athlete: {ansii['reset']}{names[max_ath]}")
    print(f"{ansii['red']}Cheater refree: {ansii['reset']}Refree{str(max_ref + 1)}")
    
    new_athletes = remove_cheaters(max_ath, max_ref, athletes)
    print(f"{ansii['green']}Champion: {ansii['reset']}{names[real_champion(new_athletes)]}")


if __name__ == "__main__":
    main()
