import sys

def deblo(n): # kvadrat
    pass

def stor(x, y): # pravokotnik
    pass

def smrekica(n): # enakostranicni trikotnik
    pass

def main():

    # Vnesi argumente kot argumente programa ali kot standardni vhod
    if len(sys.argv) > 1:
        argumenti = sys.argv[1:]
    else:
        argumenti = input().split(" ")

    if argumenti[0] == "deblo":
        deblo(int(argumenti[1]))
    elif argumenti[0] == "stor":
        stor(int(argumenti[1]), int(argumenti[2]))
    elif argumenti[0] == "smrekica":
        smrekica(int(argumenti[1]))

if __name__ == "__main__":
    main()
