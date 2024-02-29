# Zadanie 03

Táto vetva obsahuje zdrojové kódy ku **zadaniu 3** z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

Úlohou zadania je vyriešenie problému húsenkovej dráhy. Tento problém spočíva v tom, že máme húsenkovú dráhu a v nej jazdí jedna húsenka (vláčik). Húsenka má určitú kapacitu pasažierov, ktoré môže pojať. A následne máme niekoľko ľudí, ktorý čakajú na jazdu. Spravidla je `ľudí > kapacita húsenky`. Jednoducho chceme implementovať, aby ľudia čakali pred húsenkou. Keď húsenka príde ľudia môžu nastúpiť až pokiaľ húsenka nie je plná. Húsenka jazdí len naplnená a ked sa naplní vyrazí na jazdu. Keď jazda skončí pasažiery vystúpia a idú znova čakať na ďalšiu jazdu medzi ostatných. Nastupovanie funguje štýlom kto skôr príde ten skôr ide tj. ľudia sa môžu aj predbiehať.

## husenkova_draha.py

Tento zdrojový kód obsahuje implementáciu/riešenie problému húsenkovej dráhy. V riešení uvažujeme, že na dráhu čaká `N` ľudi a kapacita húsenky je `C` (Spravidla `N > C`). Následne každý pasažier chodí do skupinky, ktorá čaká na jazdu a čaká na húsenku (v kóde reprezentované ako `shared.nastupQueue.wait()`). Následne ak húsenka dokončila poslednú jazdu dá signál pasažierom, že je pripravená na ďalšiu jazdu. Následne `C` pasažierov nastúpi do húsenky, posledný dá signál húsenke, že ako posledný nastúpil a húsenka môže ísť. Húsenka urobí jazdu a príde naspäť a čaká kým pasažiery vystúpia. Následne ako aj pri nástupe posledný pasažier dá husenke signál, že je posledný, a že môže začať nástup na ďalšiu jazdu. Celá implementácia je vo `while True` cykle.

V zadaní môže nastať problém **vyhladovania**, na ktorý si treba dať pozor.

Ukážka použitia upravenej bariéry, ktorá dáva signál húsenke:

![](/img/upravena_bariera.png)

Vypis z konzoli po 2 iteráciách:

![](/img/vypis.png)


## Zdroje použité pri tvorbe kódu a dokumentácie

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár 3 PDF*

*Seminár 3 kódy z GitHub*

*[ChatGPT](https://chat.openai.com/)*

