### 8. termin <sub><sup>*(17.5.2017)*<sup><sub>
- slovar

***
#### Naloga 1
V neki datoteki imamo neko besedilo.
Tvoja naloga je, da iz besedila izluščiš terke po 2 znaka, jih prešteješ in za vsako terko določiš relativno frekvenco pojavitve v besedilu.

Pri tem misli na to, da upoštevaš le terke, ki ti dajo neko informacijo, npr. 'aa', ' a' imata neko dodano vrednost, pri čemer dvojni presledki ali nove vrstice nimajo vrednosti za nas. Poleg tega sta 'aa' in 'AA' enakovredna.

Na koncu izpiši terke po padajoči vrednosti frekvenc. Če imajo terke enako frekvenco sortiraj ravno tako padajoče po vrednosti terk, 'cc' pred 'aa'.

Prosim ne uporabljaj Counter in podobnih stvari za štetje pojavitev.

###### Primer

Vsebina besedila:
```
Aaa bcC.
```
Izhod:
```
aa 0.25
 b 0.125
c. 0.125
cc 0.125
.  0.125
bc 0.125
a  0.125
```

***
#### Dodatki za Naloga 1
Slovar:
```python
from collections import defaultdict
text = defaultdict(int)
d["prvi"] += 1
print(d["prvi"]) # 1
print(d["drugi"]) # 0
```
