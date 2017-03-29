import sys

a = "*" #for easier calling
n = "\n"

def deblo(x): # kvadrat
    print((a*x+n)*x)

def stor(x, y): # pravokotnik
    print((a*x+n)*y)

def smrekica(lays): # enakostranicni trikotnik; lays => layers
    for x in range(lays):
        print(a*x)

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
