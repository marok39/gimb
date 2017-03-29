import sys

def deblo(n): # kvadrat
    for i in range(n):
        print("*" * n)

def stor(x, y): # pravokotnik
    for i in range(y):
        print("*" * x)

def smrekica(n): # enakostranicni trikotnik
    for i in range(1, n + 1):
        print (" " * (n - i) + "*" * (i * 2 - 1))

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
