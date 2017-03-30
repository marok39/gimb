import sys

def funkcija(a, b, x):
    #a -= 1
    while a%x != 0:
        a += 1
    #b += 1
    while b%x != 0:
        b -= 1
    delta = b - a
    amount = delta//x + 1
    return amount


def main():
    if len(sys.argv) > 1:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        a = int(input())
        b = int(input())

    n = funkcija(a, b, 2) + funkcija(a, b, 3) + funkcija(a, b, 5) - funkcija(a, b, 6) - funkcija(a, b, 10) - funkcija(a, b, 12) + funkcija(a, b, 30)
    print("%d" % n)

if __name__ == "__main__":
    main()
