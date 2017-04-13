### 3. termin <sub><sup>*(12.4.2017)*<sup><sub>
- seznam (1d, 2d)
- branje/pisanje datoteke
- razred

***
#### Naloga 1
Pri tej nalogi se bomo naučili vse potrebne koncepte za reševanje ASCII art naloge.
Simulirali bomo neko osnovno trgovino, kjer se prodaja, kupuje in posodablja zalogo.

Načeloma je mišljeno, da se za vsako podtočko napiše funkcijo oz. neko funkcijo uporabi.

1. Seznam
    1. Izpiši trojice za vse artikle, npr: ```('hruska', 5, 2.99)```
    2. Poišči artikel z min ali max vrednostjo zaloge ali cene
    3. Napiši funkcijo, ki spremeni zalogo nekemu artiklu, klic bi lahko bil: ```posodobi_zalogo('jabolko', 10, ime_artikla, zaloga_artikla) # poveca zalogo jabolka za 10```
2. 2D seznam
    1. Naredi 2D seznam in napiši funkcijo, ki izpiše trojice za vse artikle
3. Razred
    1. Definiraj razred Artikel, ki ima atribute (ime, zaloga, cena)
    2. Definiraj ```__str__(self):```, ki objektu Artikel izpiše atribute v obliki trojice
    3. Razredu dodaj funkcijo, ki zviša oz. zniža zalogo
    4. Razredu dodaj funkcijo, ki preveri, če lahko iz zaloge kaj dvignemo
4. Branje datoteke v razred
    1. Preberi vsebino datoteke data.txt v nek seznam
    2. Kreiraj seznam objektov Artikel in jih napolni s podatki iz data.txt
    3. Pokliči nekaj funkcij in preveri (print), če deluje vse kot mora.
5. Simulacija trgovine in zapis zalog v datoteko
    1. Glede na input():
        - stanje : izpiši koliko smo zaslužili danes (lahko gremo v minus)
        - kupi (artikel, kolicina) : plačamo 0.5 cene artikla * kolicina in prištejemo zalogi
        - prodaj (artikel, kolicina) : dobimo ceno artikla * kolicina in odštejemo zalogi (samo, če imamo dovolj na zalogi)
        - konec : zaključi in zapiši trenutno stanje zalog v neko datoteko
    2. Po vsakem input() izpiši stanje zalog artiklov, npr. ```print(artikli)```


***
#### Dodatki
Tabele (seznami):
```python
ime_artikla = ["jabolko", "hruska", "pomaranca", "banana"]
zaloga_artikla = [10, 5, 1, 23]
cena_artikla = [1.99, 2.99, 2.49, 1.89]

a = [ime_artikla, zaloga_artikla, cena_artikla] # 2d seznam
```

Branje/pisanje datotek:
```python
# branje
with open("pot_do_datoteke", "r") as f:
  # naenkrat preberi celotno datoteko in
  # jo shrani v (verjetno) 2d seznam file_data
  file_data = f.readlines()

# pisanje
with open("pot_do_datoteke", "w") as f:
  f.write("%s\n" % "Hello") # v eno vrstico datoteke sem napisal 'Hello'
```

Razred:
```python
# Definiram razred Pravokotnik z dolžinama stranic a in b
class Pravokotnik:
  """
  Znotraj tega razreda definiramo vse funkcije, ki so povezane z objektom Pravokotnik,
  ali pa se vsaj navezujejo vsebinsko na objekt Pravokotnik (npr. kaksne staticne metode)
  """
  def __init__(self, data): # lahko tudi (self, a, b)
    """
    __init__ se klice vsakic, ko poklicemo npr.
    p = Pravokotnik((2, 3)) # pravokotnik z a=2 in b=3 -> print(p.a) # 2
    """
    self.a = data[0]
    self.b = data[1]


  def __str__(self):
    """
    Omogoca izpis objekta:
    p = Pravokotnik((1, 2))
    print(p) # izpis je enak '(1,2)'
    """
    return "(" + str(self.a) + "," + str(self.b) + ")"


  def __repr__(self):
    """
    Omogoca izpis seznama objektov:
    p = Pravokotnik((1, 2))
    l = [p, p, p]
    print(l) # izpis je enak '[(1,2), (1,2), (1,2)]'
    """
    return str(self)


  def ploscina(self):
    """
    Razredu Pravokotnik definiram funkcijo ploscina,
    ki vrne ploscino nekega pravokotnika.
    p = Pravokotnik((1, 2))
    print(p.ploscina()) # izpis je '2'
    """
    return self.a * self.b

data = (1, 2)
p = Pravokotnik(data)
l = [p, p, p]
print(p.a, p.b, p, p.ploscina())
print(l)
```
