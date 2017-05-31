import sys

def osnovna(a, b):
    """ Osnovni nacin stetja """
    n = 0
    for i in range(a, b + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            n += 1

    return n

def divX(a, b, x):
    """ Izracunaj koliko stevil na intervalu med a in b je deljivih z x. """
    while a % x != 0:
        a = a + 1
    while b % x != 0:
        b = b - 1

    dif = b - a
    div = (dif // x) + 1

    return div

def main():
    if len(sys.argv) > 1:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        a = int(input())
        b = int(input())

    # no = osnovna(a, b)

    # napredna
    n = divX(a, b, 2) + divX(a, b, 3) + divX(a, b, 5) \
        - divX(a, b, 6) - divX(a, b, 10) - divX(a, b, 15) \
        + divX(a, b, 30)

    # print("%d %d" % (no, n)) # vrneta osnovna in napredna enako?
    print("%d" % n)

if __name__ == "__main__":
    main()
