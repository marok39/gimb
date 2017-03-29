import sys

def funkcija(a, b):
    return 0

def main():
    if len(sys.argv) > 1:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        a = int(input())
        b = int(input())

    n = funkcija(a, b)
    print("%d" % n)

if __name__ == "__main__":
    main()
