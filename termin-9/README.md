### 9. termin <sub><sup>*(24.5.2017)*<sup><sub>
- osnove uporabe strojnega učenja

***
#### Naloga 1
V direktoriju ```human_rights``` so deklaracije človekovih pravic za nekaj evropskih držav. Tvoja naloga je, da na podlagi teh besedil ugotoviš kateri jeziki so si med seboj najbolj podobni.

Brez skrbi, večinoma je naloga že rešena, ti boš moral le zapisati nekaj formul in uporabiti nekaj funkcij.

Podobnost med dvema jezikoma bomo merili s kosinusno razdaljo, ki se jo izračuna takole:
![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/1e1fccd8f6d7c2acccde3c9426a795c4b9570c27 "kosinusna podobnost")

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/f8ed5fa804164749f0cb7eac4bd869458bfc8bda "kosinusna podobnost")

Ko imaš enkrat to implementirano, moraš le še za vsako kombinacijo dveh jezikov izračunati njuno medsebojno razdaljo in jo shraniti v nek seznam. Ostalo bo prevzel scipy.

Če si vse rešil pravilno bi moral dobiti nekaj takega:
![dendrogram](img/result.png)

***
#### Dodatki za Naloga 1
Potrebne knjižnjice:
```
unidecode
numpy
scipy
```
