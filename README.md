# Zadanie 04

Táto vetva obsahuje zdrojové kódy ku zadaniu 4 z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

Zadanie spočíva k úprave kódu z cvičenia, inšpirovaného z [kódu na tomto linku](https://kurzy.kpi.fei.tuke.sk/pp/labs/pp_mm.c). Našou úlohou je úprava P2P komunikácie aby fungovala a umoňila vykonanie pre ľubovoľný počet pracovných uzlov tj. že počet riadkov matice nebude musieť byť deliteľný počtom pracovných uzlov. Druhou častou zadania je pretvorenie kódu z P2P komunikácie na **kolektívnu komunikáciu** pomocou `scatter()/gather()`

## P2P_pre_n_procesov.py

Tento zdrojový kód obsahuje implementáciu/riešenie problému násobenia matíc pomocou viacerých pracovných uzlov pomocou P2P komunikácie. Riešenie je schopné použiť rôzny počet pracovných uzlov (1-8 na mojom zariadení). 

## Kolektivna_kom.py

Tento zdrojový kód obsahuje implementáciu/riešenie problému násobenia matíc pomocou viacerých pracovných uzlov pomocou kolektívnej komunikácie (`scatter()/gather()`).

## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár 7 PDF*

*Seminár 7 kódy z GitHub*

*[ChatGPT](https://chat.openai.com/)*

*[Kód z ktorého sme sa inšpirovali](https://kurzy.kpi.fei.tuke.sk/pp/labs/pp_mm.c)*
