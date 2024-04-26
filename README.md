# Zadanie 06

Táto vetva obsahuje zdrojové kódy ku zadaniu 6 z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`.

## zadanie_planovac.py

Úlohou zadania bolo vytvorenie plánovača koprogramov. Plánovač plánuje koprogrami jeden za druhým a stále dookola pokial sú vo fronte nejaké koprogrami.
Plánovač reprezentujeme ako python class.
Koprogrami do fronty pridávame pomocou metódy `add_job(it)`. Po naplnení fronty môžme plánovač spustit pomocou metódy `start()`.
Pokial sa podaktorý z koprogramov skončí (`StopIteration`) z fronty je odstránený.

Pre ukážku funčnosti plánovača sme implementovali 3 jednoduché koprogrami. Všetky koprogrami skončia v konečnom čase. **Prvý koprogram** prijíma správy v podobe náhodného čísla od 1 po 10 a vypisuje len tie čo sú nepárne (čínnosť vykoná 200 krát). **Druhý koprogram** vypisuje prvočísla do 300 a **tretí koprogram** vypisuje párne čísla do 1000. Plánovač reaguje na ukončenie koprogramu informačným výpisom, kde vypíše ktorý koprogram skončil.

Výstup pre moju implementáciu:

![](/img/output.png)


## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár PDF*

*Seminár kódy z GitHub*

*[ChatGPT](https://chat.openai.com/)*
