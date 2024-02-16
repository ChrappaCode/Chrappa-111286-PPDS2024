# Zadanie 01 

Táto vetva obsahuje zdrojové kódy ku **zadaniu 1** z PPDS.

Úlohou zadania je vyriešenie problému "**kto jedol prvý**". V zadaní sme vytvorili dve vlákna reprezentujúce `Jana` a `Fera`.

Problém "**kto jedol prvý**" spočíva v tom, že simulujeme bežné úkony tj. *spánok*, *ranná hygiena*, *telefonát* a *raňajkovanie*. Hlavnou premisou zadania je zabezpečenie aby `Jano` raňajkoval skôr ako `Fero`, tj. aby vlákno 1 vykonalo tento úkon skôr ako vlákno 2.

Na zabezpečenie požadovaného spŕavania je možné použiť niekoľko techník. V mojom vypracovaní som sa zameral hlavne na triedu `Semaphore` z knižnice [fei.ppds](https://pypi.org/project/fei.ppds/), ktorú som použil vo vypracovaní [1semafor](1semafor.py) a [2semafory](2semafory.py)
