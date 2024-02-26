# Zadanie 02

Táto vetva obsahuje zdrojové kódy ku **zadaniu 2** z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

Úlohou zadania je vyriešenie problému hodujúcich divochov. Tento jednoduchý problém spočíva v tom, že máme nejakú **konštantu** divochov pre príklad 5 a úlohou je zabezpečiť aby disosi začali jesť obed vždy spoločne tj. pred každým jedlom sa všetci piati divosi počkajú a jedia až keď prídu všetci. Ak im istý počet navareného jedla dojde, divoch, ktorý si všimne, že je hrniec prázdny povie kuchárovi, že je hrniec prázdny a kuchár navarí znova plný hrniec. Bežný deň divocha je nasledovný: Divoch príde a čaká na kamarátov, spolu sa najedia a následne idú na lov, neskôr sa opať stretnú a idú hodovať.

## divosi.py

Toto vypracovanie rieši problém hodujúcich divochov pomocou **znovopoužiteľnej bariéry**. V mojom kóde sa nachádzajú 2 konštanty `N` a `H`. `N` reprezentuje počet divochov a `H` reprezentuje veľkosť hrnca. Riešenie funguje na princípe ako je opísané v časti o úlohe zadania. V implementácií je vyžitých niekoľko `sleep()` funkcií na sprehľadnenie výpisu a simulovania dlhšieho vykonávania úkonu. 

Ďalej v implementácií ako je spomenuté vyššie sme využili znovopoužiteľnú bariéru: 


