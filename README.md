# Zadanie 01 

Táto vetva obsahuje zdrojové kódy ku **zadaniu 1** z PPDS.

Úlohou zadania je vyriešenie problému "**kto jedol prvý**". V zadaní sme vytvorili dve vlákna reprezentujúce `Jana` a `Fera`.

Problém "**kto jedol prvý**" spočíva v tom, že simulujeme bežné úkony tj. *spánok*, *ranná hygiena*, *telefonát* a *raňajkovanie*. Hlavnou premisou zadania je zabezpečenie aby `Jano` raňajkoval skôr ako `Fero`, tj. aby vlákno 1 vykonalo tento úkon skôr ako vlákno 2.

Na zabezpečenie požadovaného spŕavania je možné použiť niekoľko techník. V mojom vypracovaní som sa zameral hlavne na triedu `Semaphore` z knižnice [fei.ppds](https://pypi.org/project/fei.ppds/), ktorú som použil vo vypracovaní [1semafor](1semafor.py) a [2semafory](2semafory.py)

## 1semafor

Tento kód obsahuje vypracovanie problému použitím jedného semafóra. Jednoducho simuluje úkony spomenuté vyššie, pomocou funkcie `sleep()` simulujeme dlhšie trvanie úkonu.

Ukážka simulácie *rannej hygieny*: 

//Obrázok kódu

Podobne simuluje aj zvyšné úkony.

Následne sme vytvorili dve vlákna a im príslušné funkcie v ktorých tieto simulácie voláme s tým, že pomocou semafora sme zabezpečili aby sa vlákno 1 (`Jano`) raňajkovalo skôr.

Po spustení programu vidíme v konzole nasledujúce výpisy: 

//Obrázky

## 2semafory

Tento kód obsahuje vypracovanie problému použitím dvoch semafórov, jedného pre `Jana` a jedného pre `Fera`. Takisto ako prvý kód simuluje úkony spomenuté vyššie, pomocou funkcie `sleep()` simuluje dlhšie trvanie úkonu.

Aj toto vypracovanie ako aj prvé rieši problém "**kto jedol prvý**". Využitím druhého semafora som sa snažil sprehladniť riešenie a zabezpečiť aby `Jano` aj `Fero` začali naraz spať aj umývať sa, následne sa `Jano` naraňajkuje, zavolá `Ferovi`, `Fero` hovor príjme a naraňajkuje sa tiež.

Po spustení programu vidíme v konzole nasledujúce výpisy: 

//Obrázky
