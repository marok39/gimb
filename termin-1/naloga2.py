from math import pi, e, sqrt
import sys

def fakulteta(n):
    return 0

def rekurzivno(n):
    return 0

def stirling(n):
    return 0

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input())

    print("%10s | %20s | %20s | %25s | %7s" % \
        ("n", "fakulteta", "rekurzija", "stirling", "napaka"))
    for i in range(1, n + 1):
        f, r, s = fakulteta(i), rekurzivno(i), stirling(i)
        
        e = 0 # izracunaj se relativno napako
        
        print("%10d | %20d | %20d | %25.5f | %5.5f" % (i, f, r, s, e))

if __name__ == "__main__":
    main()
