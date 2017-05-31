from time import time
from random import randint

def main():
    """
    Igra hitre postevanke.
    Vnesi stevilo krogov, ki jih zelis igrati.
    Program ti bo naključno dal za zmnoziti dve stevili (1<=x<=10),
    pri tem pa meril cas.
    """

    n = int(input("Vnesi stevilo krogov: "))
    correct = 0

    start = time()

    for i in range(1, n + 1):
        a = randint(1, 10)
        b = randint(1, 10)
        c = a * b

        res = int(input("Izracunaj: " +  str(a) + " * " + str(b) + " = "))

        if res == c:
            print("Pravilno! :)")
            correct += 1
        else:
            print("Napacno! :(")

    end = time()

    print("Pravilno si odgovoril/a na", correct, "/", n, \
        "za kar si porabil/a", "{:.2f}".format(end - start), "s.")

if __name__ == "__main__":
    main()
