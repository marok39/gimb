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
#### Testiranje rešitev
Za testiranje rešitev so priloženi testni primeri, ki jih preverite ročno ali pa uporabite priloženo python skripto.

Primer ročnega preverjanja:

```python3 naloga1.py < test-1/input-1 > test-1/output-1```

Primer uporabe skripte:

```python3 tp.py naloga1```
