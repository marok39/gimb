import sys
from math import floor

a = "*" #for easier calling
n = "\n"
s = " "


def deblo(x): # kvadrat
    print((a*x+n)*x)


def stor(x, y): # pravokotnik
    print((a*x+n)*y)


def smrekica(lays): # enakostranicni trikotnik; lays => layers
#    for x in range(lays+1):
#        print(s*(lays-x) + (a*(x-1) + a))
    for i in range(1,lays*2,2):
        print("{}".format(a*i).center(lays*2))


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
