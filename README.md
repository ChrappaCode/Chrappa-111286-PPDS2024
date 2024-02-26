# Zadanie 02

Táto vetva obsahuje zdrojové kódy ku **zadaniu 2** z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

Úlohou zadania je vyriešenie problému hodujúcich divochov. Tento jednoduchý problém spočíva v tom, že máme nejakú **konštantu** divochov pre príklad 5 a úlohou je zabezpečiť aby disosi začali jesť obed vždy spoločne tj. pred každým jedlom sa všetci piati divosi počkajú a jedia až keď prídu všetci. Ak im istý počet navareného jedla dojde, divoch, ktorý si všimne, že je hrniec prázdny povie kuchárovi, že je hrniec prázdny a kuchár navarí znova plný hrniec. Bežný deň divocha je nasledovný: Divoch príde a čaká na kamarátov, spolu sa najedia a následne idú na lov, neskôr sa opať stretnú a idú hodovať.

## divosi.py

Toto vypracovanie rieši problém hodujúcich divochov pomocou **znovopoužiteľnej bariéry**. V mojom kóde sa nachádzajú 2 konštanty `N` a `H`. `N` reprezentuje počet divochov a `H` reprezentuje veľkosť hrnca. Riešenie funguje na princípe ako je opísané v časti o úlohe zadania. V implementácií je vyžitých niekoľko `sleep()` funkcií na sprehľadnenie výpisu a simulovania dlhšieho vykonávania úkonu. 

Ďalej v implementácií ako je spomenuté vyššie sme využili znovopoužiteľnú bariéru: 

![](/img/bariera.png)

Znovopoužiteľná bariéra sa skladá z dvoch jednoduchých bariér. Princípom jednoduchej bariéry je, že na začiatku je *turniket* (`Semaphore`) zablokovaný. N-té vlákno, ktoré k *turniketu* príde, *turniket* odblokuje pre N vlákien, ktoré následne všetky prejdú *bariérov*. Ako na obrázku vyššie vidno takúto jednoduchú bariéru sme implementovali 2 krát po sebe z dvôvodu znovopoužiteľnosti, práve preto, že náš kód beží vo `while True` cykle a môže pri použití len jednej jednoduchej bariéry v dôsledku preplánovania vlákien prísť ku uviaznutiu vlákna. 

![](/img/mutex_integrita.png)

V tejto ukážke kódu ako aj v minulej je použitý `Mutex()`. Mutex v implementácií používame na miestach kde vlákna menia počet niečoho. Na prvom obrázku to je počítadlo vlákien, ktoré čakajú na bariére a v tomto prípade je to hrniec a odčítavanie porcií. Dôvodom použitia mutexu je zachovanie integrity týchto počítadiel.

![](/img/kuchar_rande.png)

![](/img/varenie.png)

V ďaľších dvoch fragmentoch kódu je ukázaná časť kde si divoch všimne, že už nie je žiadne navarené jedlo, dá signál kuchárovi, ktorý zatiaľ na signál čakal, ten následne jedlo navarí (naplní hrniec konštantou `H`) a divochovi čo čaká u prázdenho hrnca dá signál, že už je dovarené a divosi môžu ďalej hodovať (Tieto vzory sú implementované pomocou `Sempahoru` inicializovaného na 0). 

Ukážka výpisu programu v iterácií, v ktore si divoch všimne, že je hrniec prázdny:

![](/img/vypis.png)

Vo výpise je vidieť, že všetkých `N` vláknie (divochov) sa na začiatku počká náslene idú hodovať. V momente čo si divoch všimne, že už neni v hrnci žiadna porcia povie kuchárovi, že má navariť, kuchár navarí a hostina môže pokračovať.

## Zdroje

