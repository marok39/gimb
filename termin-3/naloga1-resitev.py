"""
======================================================================
Metode za tocki 1 in 2
======================================================================
"""
def izpisi_trojice(ime, zaloga, cena):
    for i in range(len(ime)):
        print((ime[i], zaloga[i], cena[i]))
        # print("(", ime[i], ",", zaloga[i], ",", cena[i], ")")

def izpisi_trojice_2d(a):
    for i in range(len(a)):
        print((a[0][i], a[1][i], a[2][i]))

def izpisi_min(ime, l):
    # poisci min
    min_ime = ime[0]
    min_vrednost = l[0]
    for i in range(1, len(ime)):
        tmp = l[i]
        if tmp < min_vrednost: # tmp > max_vrednost, ce zelimo max
            min_ime = ime[i]
            min_vrednost = tmp

    print("min vrednost ima artikel", min_ime, ":", min_vrednost)

def posodobi_zalogo(artikel, kolicina, ime_artikla, zaloga_artikla):
    for i in range(len(ime_artikla)):
        if artikel == ime_artikla[i]:
            zaloga_artikla[i] += kolicina
            return zaloga_artikla

def main_osnovno():
    """ vsebina data.txt
    artikel zaloga cena
    jabolko 10 1.99
    hruska 5 2.99
    pomaranca 1 2.49
    banana 23 1.89
    """
    ime_artikla = ["jabolko", "hruska", "pomaranca", "banana"]
    zaloga_artikla = [10, 5, 1, 23]
    cena_artikla = [1.99, 2.99, 2.49, 1.89]

    print("Nasi artikli (ime, zaloga, cena):")
    izpisi_trojice(ime_artikla, zaloga_artikla, cena_artikla) # 1.1
    print("Min zaloge:")
    izpisi_min(ime_artikla, zaloga_artikla) # 1.2 minmax zaloge
    print("Min cene (v €):")
    izpisi_min(ime_artikla, cena_artikla) # 1.2 minmax cene

    # 1.3
    print("Posodobi zalogo jabolk - pred posodobitvijo je", zaloga_artikla[0])
    zaloga_artikla = posodobi_zalogo("jabolko", 1, ime_artikla, zaloga_artikla)
    print("Po dodajanju enega artikla je", zaloga_artikla[0])
    zaloga_artikla = posodobi_zalogo("jabolko", -3, ime_artikla, zaloga_artikla)
    print("Po odvzemanju 3 artiklov je", zaloga_artikla[0])

    # 1.4
    izpisi_trojice(ime_artikla, zaloga_artikla, cena_artikla)
    zaloga_artikla = posodobi_zalogo("jabolko", -8, ime_artikla, zaloga_artikla)
    izpisi_trojice(ime_artikla, zaloga_artikla, cena_artikla)

    # 2.1
    artikli = [ime_artikla, zaloga_artikla, cena_artikla]
    izpisi_trojice_2d(artikli)

"""
===========================================================
Metode za resitev z razredom in branje/pisanje datoteke
===========================================================
"""

class Artikel:
    def __init__(self, data):
        self.ime = data[0]
        self.zaloga = data[1]
        self.cena = data[2]


    def __str__(self):
        return "(" + str(self.ime) + "," + str(self.zaloga) + "," + str(self.cena) + ")"


    def __repr__(self):
        return str(self)


    def to_file_str(self):
        return self.ime + " " + str(self.zaloga) + " " + str(self.cena)


    def preveri_zalogo(self, kolicina=1):
        if self.zaloga - kolicina >= 0:
            return True
        return False


    def dodaj(self, kolicina=1):
        if kolicina >= 0:
            self.zaloga += kolicina
            return True
        return False


    def zmanjsaj(self, kolicina=1):
        if self.preveri_zalogo(kolicina):
            self.zaloga -= kolicina
            return True
        return False


def main():
    with open("test-1/data/data.txt", "r") as f:
        indata = f.readlines()
    data = indata[1:]

    artikli = []
    for line in data:
        a_data = line.split()
        a_data = (a_data[0], int(a_data[1]), float(a_data[2]))
        a = Artikel(a_data)
        artikli.append(a)

    stanje = 0
    print(artikli)
    ukaz = input("Izberi moznost (kupi, prodaj, stanje ali konec): ")
    while ukaz != 'konec':
        if ukaz == 'kupi':
            koga = input("Koga? ")
            koliko = int(input("Koliko? "))
            for item in artikli:
                if item.ime == koga:
                    if item.dodaj(koliko):
                        stanje -= koliko * item.cena * 0.5
                    break
        elif ukaz == 'prodaj':
            koga = input("Koga? ")
            koliko = int(input("Koliko? "))
            for item in artikli:
                if item.ime == koga:
                    if item.zmanjsaj(koliko):
                        stanje += koliko * item.cena
                    break
        elif ukaz == 'stanje':
            print("Zasluzili smo:", "{:.2f}".format(stanje), "€.")
        print(artikli)
        ukaz = input("Izberi moznost (kupi, prodaj, stanje ali konec): ")

    with open("test-1/data/new_data.txt", "w") as f:
        f.write("%s\n" % "artikel zaloga cena")
        for a in artikli:
            f.write("%s\n" % a.to_file_str())

if __name__ == "__main__":
    # main_osnovno()
    main()
