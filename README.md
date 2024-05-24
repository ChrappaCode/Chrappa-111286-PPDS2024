# Zadanie 07

Táto vetva obsahuje zdrojové kódy ku zadaniu 7 z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

## zadanie.py

Úlohou zadanie bolo vytvoriť asynchrónnu aplikáciu, ktorá bude schopná sťahovať súbory cez protokol HTTP(S) a zobrazovať priebežný stav sťahovania vo forme vizuálneho progress baru. Aplikácia by mala byť schopná sťahovať niekoľko súborov naraz, čo sa mi v implementácií podarilo a implementácia je schopná sťahovať niekoľko súborov naraz (nie je limitovaná len na 2). Na vizualizáciu progress baru som použil knižnicu `tqdm`. Pre asynchrónne požiadavky a spracovanie, knižnice `aiohttp` a `asyncio`. Stiahnuté súbory sa uložia na disk do priečinku, v ktorom sa nachádza aj implementácia programu.

Ukážka behu programu:

![](/img/output_bar.png)

Ukážka stiahnutých súborov:

![](/img/stiahnute.png)

Ukážka otvoreného súboru:

![](/img/ukazka_stiahnutej.png)


## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár PDF*

*[Súbory použité na testovanie programu](https://ploszek.com/ppds/)*

*[ChatGPT](https://chat.openai.com/)*
