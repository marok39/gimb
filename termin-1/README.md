### 1. termin <sub><sup>*(29.3.2017)*<sup><sub>
- uporaba konzole (```pwd, ls, cd, python3```)
  - ```pwd``` prikaže celotno pot do trenutnega imenika
  - ```ls ``` prikaže datoteke v trenutnem direktoriju:
    - ```ls -l``` ali ```ll``` seznam datotek s podrobnostmi
  - ```dir``` prikaže datoteke v trenutnem direkturiju (windows)
  - ```cd``` spremeni direktorij:
    - ```cd ..``` pojdi po hiearhiji nazaj
    - ```cd ime-mojega-direktorija``` pojdi v *ime-mojega-direktorija*
  - ```python3 ime-programa``` s python3 zaženi program *ime-programa*
- osnoven git workflow (```git pull, status, add, commit, push```)
- python3
  - std branje/pisanje
  - boolean algebra in aritmetika
  - kontrola toka (```if, while, for```)
  - funkcije

***
#### Naloga 1
Za ogrevanje bomo risali (z znakom '*') kvadrate, pravokotnike in trikotnike.
Za to imamo tri funkcije:
- deblo

Primer vhoda:    
```
python3 naloga1.py deblo 2
```

Primer izhoda:   
```
**
**
```
- stor

Primer vhoda:    
```
python3 naloga1.py stor 3 1
```

Primer izhoda:   
```
***
```
- smrekica

Primer vhoda:    
```
python3 naloga1.py smrekica 5
```

Primer izhoda:   
```
    *
   ***
  *****
 *******
*********
```
***
#### Naloga 2
Napiši tri funkcije za različne načine izračuna vrednosti fakultete.
Vrednost fakultete se izračuna takole:
```
5! = 5 * 4 * 3 * 2 * 1
0! = 1 (izhaja iz definicije)
```
- iterativno

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/a7c28fa7a3b7ed2244d5d3f88ef0dc289a25b643 "fakulteta iteracija")
- rekurzivno

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/0aa940d197f80ace5839c8596a61ae3e00a5e260 "fakulteta rekurzija")
- približek (Stirling)

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/15b10f6b044657c32e5572151e17880fa78bb5e8 "Stirling formula")

Izračunaj še relativno napako med natančno in približno vrednostjo fakultete.
Za konec lahko v tabeli izpišeš prvih n vrednosti fakultete.
Za avtomatsko preverjanje uporabi izpis kot v predlogi.

Primer vhoda:    
```
python3 naloga2.py
5
```

Primer izhoda:   
```
         n |            fakulteta |            rekurzija |                  stirling |  napaka
         1 |                    1 |                    1 |                   0.92214 | 0.07786
         2 |                    2 |                    2 |                   1.91900 | 0.04050
         3 |                    6 |                    6 |                   5.83621 | 0.02730
         4 |                   24 |                   24 |                  23.50618 | 0.02058
         5 |                  120 |                  120 |                 118.01917 | 0.01651
```

***
#### Testiranje rešitev
Za testiranje rešitev so priloženi testni primeri, ki jih preverite ročno ali pa uporabite priloženo python skripto.

Primer ročnega preverjanja:

```python3 naloga1.py < test-1/input-1 > test-1/output-1```

Primer uporabe skripte:

```python3 tp.py naloga1```
