from time import time as t
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
        except:
            pass
    total, correct = timeFunc(x)
    print("V {:.3} sekundah ste pravilno odgovorili na {} od {}, kar je {}%. \
V povprecju ste porabili {:.3} na krog.".format(total, correct, x, correct*100/x, total/x))

def mult(amount):
    correct = 0
    for x in range(1, amount+1):
        a = randint(1, 11)
        b = randint(1, 11)
        try:
            numb = int(input("Zmnozi: {} * {} = ".format(a, b)))
        except:
            pass
        if numb == a * b:
            correct +=1
    return correct

def timeFunc(x):
    start = t()
    funcret = mult(x)
    end = t() - start
    return (end, funcret)

if __name__ == "__main__":
    main()
