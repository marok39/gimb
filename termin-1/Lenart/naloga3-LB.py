from time import time
from random import randint

def main():
    """
    Igra hitre postevanke.
    Vnesi stevilo krogov, ki jih zelis igrati.
    Program ti bo naključno dal za zmnoziti dve stevili (1<=x<=10),
    pri tem pa meril cas.
    """
    while True:
        try:
            x = int(input("Vnesi stevilo krogov:\n"))
            break
    total, correct = time(mult, x)
    print("V {} ste pravilno odgovorili na {} od {}, kar je {}%".format(total, correct, x, correct/x))

def mult(amount):
    correct = 0
    for x in range(amount+1):
        a = randint(1, 11)
        b = randint(1, 11)
        try:
            numb = int(input("Zmnozi: {} * {} = ".format(a, b)))
        if numb == a * b:
            correct +=1
    return correct

def time(func, x):
    start = time()
    funcret = func(x)
    return (time() - start, funcret)

if __name__ == "__main__":
    main()
