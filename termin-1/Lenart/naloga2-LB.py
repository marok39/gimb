from math import pi, e, sqrt
import sys

def fakulteta(n):
    temp = 1
    for x in range(n+1):
        temp *= x
    return temp

def rekurzivno(n):
    if n == 0:
        return 1
    else:
        return n * rekurzivno(n-1)

def stirling(n):
    return(sqrt(2*pi*n)*(n/e)^n)

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input())

    print("%10s | %20s | %20s | %25s | %7s" % \
        ("n", "fakulteta", "rekurzija", "stirling", "napaka"))
    for i in range(1, n + 1):
        f, r, s = fakulteta(i), rekurzivno(i), stirling(i)

        rel = 1 - 1/(rekurzivno(i)/stirling(i))

        print("%10d | %20d | %20d | %25.5f | %5.5f" % (i, f, r, s, rel))

if __name__ == "__main__":
    main()
