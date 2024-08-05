def get_name(v: int) -> str:

    while True:
        try:
            name = input(f"Enter name {v}: ")
            if len(name) == 0:
                print("Invalid input") 
            else: 
                return name
        except ValueError:
            print("Invalid input")

def main():

    c_ali = 0
    c_six = 0
    c_k = 0
    for i in range(50):
        name = get_name(i + 1)
        if name == 'ali':
            c_ali += 1
        if len(name) == 6:
            c_six += 1
        if name[0] == 'k':
            c_k += 1
    
    print(f"A: {c_ali}")
    print(f"B: {c_six}")
    print(f"C: {c_k}")





if __name__ == "__main__":
    main()