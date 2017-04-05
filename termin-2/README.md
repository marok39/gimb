### 2. termin <sub><sup>*(5.4.2017)*<sup><sub>
- python3
  - std branje/pisanje
  - boolean algebra in aritmetika
  - kontrola toka (```if, while, for```)
  - funkcije
- rekurzija

***
#### Naloga 1
Igrali se bomo igro hitre poštevanke.
Napiši program, ki mu podaš število krogov igre, program pa ti za vsak krog naključno generira poštevanko, ki jo moraš kar se da hitro rešiti.
Po zadnjem krogu izpiši število pravilnih odgovorov in čas, ki si ga pri tem porabil.
Predlagam interval naključnih števil [1, 10].

Primer enega kroga:
<pre>Izracunaj: 2 * 2 = <i>(moj vnos)</i></pre>

***
#### Naloga 2
Napiši program, ki vrne število števil, ki so deljiva z 2, 3 ali 5 na intervalu [a, b].

Primer vhoda:    
```
python3 naloga4.py
4
12
```

Primer izhoda:   
```
7
```
To so števila: ```4, 5, 6, 8, 9, 10, 12```

Testna primera 4 in 5 sta malo težja (večji interval). Poskusi dobiti rešitev v manj kot 5 sekundah.
***
#### Naloga 3 (za pogumne)
Napiši program, ki sliko iz formata PPM pretvori v ASCII art.
Osnovni algoritem, gre nekako takole: vsako piko (piksel) prvotne slike pretvori v sivinsko vrednost tako, da izračunaš povprečje R, G, B.

Tako je sivina:
```
sivina = (R + G + B) / 3
```

Vsaki sivini se nato priredi ASCII znak, ki pokrije znakovno polje (od bele proti črni) in vrednost sivine, ki ji znak pripada:
```
Z = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
S = (230, 200, 180, 160, 130, 100, 70 , 50)
za i = 0...7:
  če sivina >= S[i] => znak = Z[i]
```
Za nadgradnjo lahko vsak piksel izhodne datoteke zavzema več pikslov vhodne PPM datoteke (tako zmanjšamo ASCII sliko). Velikost 'okna' bo tako n x n.

V datotekah input-* so 3 vrstice:
```
ime slike
ime izhodne ascii slike
velikost okna
```
V izhodno datoteko izpišite zgolj ASCII sliko.

Več o formatu PPM najdete [tukaj](http://netpbm.sourceforge.net/doc/ppm.html).

V osnovi pa izgleda takole; opisujemo sliko enega belega piksla:
```
P6            (definira format)
1 1           (sirina x visina)
255           (max vrednost barve)
255 255 255   (RGB vrednosti enega piksla)
```
Za boljšo preglednost predlagam, da za predstavitev enega piksla uporabite razred.
Za pomoč pri branju si lahko pomagate z ```ascii.py``` (kjer je rešen težji del naloge).
***
#### Testiranje rešitev
Za testiranje rešitev so priloženi testni primeri, ki jih preverite ročno ali pa uporabite priloženo python skripto.

Primer ročnega preverjanja:

```python3 naloga1.py < test-1/input-1 > test-1/output-1```

Primer uporabe skripte:

```python3 tp.py naloga1```
